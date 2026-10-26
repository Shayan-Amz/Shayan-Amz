#!/usr/bin/env node
/*
 * run_text_track.js — batch runner for the TEXT track of the thesis evaluation
 * (reference text → LLM → structured fields). Produces a runs JSON file in the
 * same shape the browser tool (academic/evaluation/app.js) exports, so that
 * evaluate.js / metrics.summarize() can score it together with voice runs.
 *
 *   OPENROUTER_API_KEY=sk-or-... node run_text_track.js \
 *       --cases cases.v2.json --prompt jarvis-prompt30.txt \
 *       --model google/gemma-4-26b-a4b-it:free --out results/text-track.json
 *
 *   node run_text_track.js --mock            # offline self-test: returns gold → F1 must be 1.0
 *
 * Rules kept identical to src/api.php (jarvisProcess): same system prompt file,
 * response_format json_object, fence stripping, params must be an object.
 * No answer repair: whatever the model returns is scored as-is.
 */
'use strict';
const fs = require('fs');
const path = require('path');
const M = require('./metrics.js');

const args = Object.fromEntries(process.argv.slice(2).map((a, i, arr) =>
  a.startsWith('--') ? [a.slice(2), arr[i + 1] && !arr[i + 1].startsWith('--') ? arr[i + 1] : true] : []).filter(x => x.length));

const casesPath = args.cases || path.join(__dirname, 'cases.v2.json');
const promptPath = args.prompt || path.join(__dirname, 'jarvis-prompt30.txt');
const model = args.model || process.env.OPENROUTER_MODEL || 'google/gemma-4-26b-a4b-it:free';
const endpoint = args.endpoint || 'https://openrouter.ai/api/v1/chat/completions';
const outPath = args.out || path.join(__dirname, 'results', `text-track-${new Date().toISOString().slice(0, 10)}.json`);
const participant = args.participant || 'P01';
const repeats = Number(args.repeats || 1);
const delayMs = Number(args.delay || 1500);          // be gentle with free-tier rate limits
const mock = Boolean(args.mock);
const apiKey = process.env.OPENROUTER_API_KEY || '';

if (!mock && !apiKey) { console.error('OPENROUTER_API_KEY is not set (or use --mock).'); process.exit(2); }

const dataset = JSON.parse(fs.readFileSync(casesPath, 'utf8'));
const systemPrompt = fs.readFileSync(promptPath, 'utf8');
const experimentId = `text-${Date.now().toString(36)}`;
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function callModel(text, useJson) {
  if (mock) {                                       // offline: echo the gold labels (sanity check of the scorer)
    const c = dataset.cases.find(x => x.reference === text);
    return { http: 200, ms: 1, body: { choices: [{ message: { content: JSON.stringify({ ai_message: 'mock', action: Object.keys(c.gold).length ? 'openPropertyModal' : null, params: c.gold }) } }], model } };
  }
  const payload = { model, provider: { allow_fallbacks: true }, messages: [{ role: 'system', content: systemPrompt }, { role: 'user', content: text }] };
  if (useJson) payload.response_format = { type: 'json_object' };
  const started = performance.now();
  const controller = new AbortController(); const t = setTimeout(() => controller.abort(), 45000);
  try {
    const res = await fetch(endpoint, { method: 'POST', signal: controller.signal,
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${apiKey}`, 'HTTP-Referer': 'https://amlak-e-man.ir', 'X-Title': 'Amlak Man thesis eval' },
      body: JSON.stringify(payload) });
    const body = await res.json().catch(() => null);
    return { http: res.status, ms: performance.now() - started, body };
  } catch (e) { return { http: 0, ms: performance.now() - started, error: e.message }; }
  finally { clearTimeout(t); }
}

function parseContent(content) {
  const cleaned = String(content).replace(/```json\s*/g, '').replace(/```\s*/g, '').trim();
  let parsed = null; try { parsed = JSON.parse(cleaned); } catch (_) { return { ok: false, error: 'invalid JSON', raw: cleaned }; }
  if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed) || !parsed.params || typeof parsed.params !== 'object' || Array.isArray(parsed.params))
    return { ok: false, error: 'params missing or not an object', raw: cleaned };
  return { ok: true, params: parsed.params, action: parsed.action ?? null, ai_message: parsed.ai_message ?? null };
}

(async () => {
  const runs = [];
  const order = [];
  for (let r = 0; r < repeats; r++) for (const c of dataset.cases) order.push(c);
  let i = 0;
  for (const c of order) {
    i++;
    const run = { id: `${experimentId}-${i}`, experiment_id: experimentId, case_id: c.id, case_snapshot: JSON.parse(JSON.stringify(c)),
      dataset_version: dataset.version, participant, mode: 'text', condition: 'not-applicable', started_utc: new Date().toISOString(),
      metadata: { llm_model: model, runner: 'run_text_track.js', mock }, status: 'running', error: null };
    const pipelineStart = performance.now();
    // same ladder as api.php: with json_object first, then without (many free models reject the parameter)
    let attempt = await callModel(c.reference, true);
    let attempts = [`json:${attempt.http}`];
    if (attempt.http === 400 || attempt.http === 404) { attempt = await callModel(c.reference, false); attempts.push(`plain:${attempt.http}`); }
    const content = attempt.body?.choices?.[0]?.message?.content;
    run.llm = { ok: false, result: { model_requested: model, model_returned: attempt.body?.model ?? null, server_ms: attempt.ms, http: attempt.http, attempts, params: null } };
    if (attempt.http === 200 && typeof content === 'string') {
      const parsed = parseContent(content);
      if (parsed.ok) {
        run.llm.ok = true; run.llm.result.params = parsed.params; run.llm.result.action = parsed.action;
        run.extraction_input = c.reference;
        run.raw_field_score = M.fieldScore(c, parsed.params);
        run.final_field_score = run.raw_field_score;        // no human correction in the batch track
        run.status = 'completed';
      } else { run.status = 'failed'; run.failed_at = 'llm'; run.error = parsed.error; run.llm.result.raw = parsed.raw; }
    } else { run.status = 'failed'; run.failed_at = 'llm'; run.error = attempt.error || `HTTP ${attempt.http}`; run.error_http = attempt.http; run.llm.result.raw = JSON.stringify(attempt.body ?? null).slice(0, 800); }
    run.client_pipeline_ms = performance.now() - pipelineStart; run.workflow_ms = run.client_pipeline_ms; run.ended_utc = new Date().toISOString();
    runs.push(run);
    const s = run.raw_field_score;
    console.log(`${run.case_id.padEnd(4)} ${run.status.padEnd(9)} ${s ? `tp=${s.tp} fp=${s.fp} fn=${s.fn} f1=${s.f1.toFixed(2)}${s.exact_match ? ' ✓' : ''}` : run.error} (${Math.round(attempt.ms)} ms)`);
    if (attempt.http === 429 || attempt.http === 402) { console.error('Quota/rate limit hit — stopping; partial results are kept.'); break; }
    if (!mock) await sleep(delayMs);
  }
  fs.mkdirSync(path.dirname(outPath), { recursive: true });
  fs.writeFileSync(outPath, JSON.stringify({ schema: 'amlak-thesis-eval-runs', experiment_id: experimentId, dataset_version: dataset.version,
    scoring: { version: 'fa-pilot-v1', note: 'fieldScore/wordError from academic/evaluation/metrics.js, unchanged.' }, generated_utc: new Date().toISOString(), runs }, null, 2));
  const summary = M.summarize(runs);
  for (const [k, v] of Object.entries(summary)) console.log(`\n${k}\n  completed ${v.completed}/${v.started}  P=${fmt(v.fields_micro.precision)} R=${fmt(v.fields_micro.recall)} F1=${fmt(v.fields_micro.f1)}  exact=${fmt(v.raw_exact_success_all_runs)}  llm p50=${ms(v.llm_service_ms_success.p50)} p95=${ms(v.llm_service_ms_success.p95)}`);
  console.log(`\nwritten: ${outPath}`);
})();
function fmt(x) { return x == null ? '—' : (100 * x).toFixed(1) + '%'; }
function ms(x) { return x == null ? '—' : Math.round(x) + 'ms'; }
