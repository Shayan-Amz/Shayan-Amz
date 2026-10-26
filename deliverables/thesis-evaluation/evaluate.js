#!/usr/bin/env node
/*
 * evaluate.js — score one or more exported run files with the unchanged thesis
 * metrics (academic/evaluation/metrics.js) and print a Markdown report.
 *
 *   node evaluate.js results/*.json            # Markdown to stdout
 *   node evaluate.js results/*.json --md results/README.md --json results/summary.json
 *   node evaluate.js results/*.json --per-field   # add per-field P/R/F1 table
 *
 * Accepts: files written by run_text_track.js ({runs:[...]}), the browser tool
 * export (array of runs or {runs}), or several of them (merged, de-duplicated by run.id).
 */
'use strict';
const fs = require('fs');
const M = require('./metrics.js');

const argv = process.argv.slice(2);
const opt = {}; const files = [];
for (let i = 0; i < argv.length; i++) {
  if (argv[i] === '--md') opt.md = argv[++i];
  else if (argv[i] === '--json') opt.json = argv[++i];
  else if (argv[i] === '--per-field') opt.perField = true;
  else files.push(argv[i]);
}
if (!files.length) { console.error('usage: node evaluate.js <runs.json ...> [--md out.md] [--json out.json] [--per-field]'); process.exit(2); }

const seen = new Set(); const runs = []; const datasets = new Set();
for (const f of files) {
  const raw = JSON.parse(fs.readFileSync(f, 'utf8'));
  const list = Array.isArray(raw) ? raw : (raw.runs || []);
  if (raw.dataset_version) datasets.add(raw.dataset_version);
  for (const r of list) { if (r.dataset_version) datasets.add(r.dataset_version); if (!seen.has(r.id)) { seen.add(r.id); runs.push(r); } }
}

const pct = x => x == null ? '—' : (100 * x).toFixed(1) + ' %';
const ms = x => x == null ? '—' : Math.round(x) + ' ms';
const ci = (k, n) => { // Wilson 95 % interval for a proportion
  if (!n) return '—'; const z = 1.96, p = k / n, d = 1 + z * z / n, c = p + z * z / (2 * n), h = z * Math.sqrt(p * (1 - p) / n + z * z / (4 * n * n));
  return `${pct((c - h) / d)}–${pct((c + h) / d)}`;
};

const summary = M.summarize(runs);
const lines = [];
lines.push(`# Thesis evaluation — results`, ``, `Generated ${new Date().toISOString()} from ${files.length} file(s), ${runs.length} runs, dataset version(s): ${[...datasets].join(', ') || 'n/a'}.`, ``);
lines.push(`Metrics are computed by the unchanged \`metrics.js\` of the repository (micro-averaged field P/R/F1 over 16 schema fields, exact-match rate, word-level Levenshtein WER for voice runs). Latencies are server-side service times unless stated.`, ``);
lines.push(`| mode | condition | ASR model | LLM model | runs | completed | fields P | fields R | **fields F1** | exact match (95 % CI) | WER | LLM p50 / p95 | pipeline p50 |`);
lines.push(`|---|---|---|---|---:|---:|---:|---:|---:|---|---:|---|---|`);
for (const [key, g] of Object.entries(summary)) {
  const [mode, cond, asr, llm] = key.split('|');
  const exactK = Math.round((g.raw_exact_success_all_runs ?? 0) * g.started);
  lines.push(`| ${mode} | ${cond} | ${asr || '—'} | ${llm || '—'} | ${g.started} | ${g.completed} | ${pct(g.fields_micro.precision)} | ${pct(g.fields_micro.recall)} | **${pct(g.fields_micro.f1)}** | ${pct(g.raw_exact_success_all_runs)} (${ci(exactK, g.started)}) | ${g.asr_scored ? pct(g.wer_micro) : '—'} | ${ms(g.llm_service_ms_success.p50)} / ${ms(g.llm_service_ms_success.p95)} | ${ms(g.client_pipeline_ms_success.p50)} |`);
}
lines.push(``, `tp/fp/fn per group: ` + Object.entries(summary).map(([k, g]) => `\`${k}\` → ${g.fields_micro.tp}/${g.fields_micro.fp}/${g.fields_micro.fn}`).join('; '), ``);

if (opt.perField) {
  const perField = {};
  for (const r of runs) {
    if (!r.raw_field_score || !r.case_snapshot) continue;
    const c = r.case_snapshot; const pred = r.llm?.result?.params || {};
    for (const key of Object.keys(M.fields)) {              // exact fieldScore rules, one field at a time
      const acc = (perField[key] ||= { tp: 0, fp: 0, fn: 0, support: 0 });
      const hasGold = Object.prototype.hasOwnProperty.call(c.gold, key);
      const sub = M.fieldScore({ gold: hasGold ? { [key]: c.gold[key] } : {}, aliases: c.aliases ? { [key]: c.aliases[key] } : undefined },
        Object.prototype.hasOwnProperty.call(pred, key) ? { [key]: pred[key] } : {});
      acc.tp += sub.tp; acc.fp += sub.fp; acc.fn += sub.fn; if (hasGold) acc.support++;
    }
  }
  lines.push(`## Per-field (all scored runs pooled)`, ``, `| field | support | tp | fp | fn | P | R | F1 |`, `|---|---:|---:|---:|---:|---:|---:|---:|`);
  for (const [k, a] of Object.entries(perField)) {
    const P = a.tp + a.fp ? a.tp / (a.tp + a.fp) : null, R = a.tp + a.fn ? a.tp / (a.tp + a.fn) : null, F = 2 * a.tp + a.fp + a.fn ? 2 * a.tp / (2 * a.tp + a.fp + a.fn) : null;
    lines.push(`| ${k} | ${a.support} | ${a.tp} | ${a.fp} | ${a.fn} | ${pct(P)} | ${pct(R)} | ${pct(F)} |`);
  }
  lines.push(``, `_Per-field rows apply fieldScore to one field at a time; their tp/fp/fn sum to the micro totals above._`, ``);
}

const failed = runs.filter(r => r.status !== 'completed');
if (failed.length) {
  lines.push(`## Failed / cancelled runs (${failed.length})`, ``, `| run | case | status | stage | error |`, `|---|---|---|---|---|`);
  for (const r of failed) lines.push(`| ${r.id} | ${r.case_id} | ${r.status} | ${r.failed_at || '—'} | ${String(r.error || '').replace(/\|/g, '\\|').slice(0, 120)} |`);
  lines.push(``);
}
const misses = runs.filter(r => r.raw_field_score && !r.raw_field_score.exact_match);
if (misses.length) {
  lines.push(`## Non-exact extractions (${misses.length})`, ``, `| run | case | tp | fp | fn | f1 | mismatched fields |`, `|---|---|---:|---:|---:|---:|---|`);
  for (const r of misses) {
    const s = r.raw_field_score; const bad = [...(s.mismatches || []).map(d => `${d.field} (exp ${JSON.stringify(d.expected)} got ${JSON.stringify(d.actual)})`), ...(s.extras || []).map(d => `+${d.field}=${JSON.stringify(d.actual)}`)].join('; ').replace(/\|/g, '\\|');
    lines.push(`| ${r.id} | ${r.case_id} | ${s.tp} | ${s.fp} | ${s.fn} | ${s.f1.toFixed(2)} | ${bad || '—'} |`);
  }
  lines.push(``);
}
const md = lines.join('\n');
if (opt.md) fs.writeFileSync(opt.md, md); else process.stdout.write(md + '\n');
if (opt.json) fs.writeFileSync(opt.json, JSON.stringify({ generated_utc: new Date().toISOString(), files, runs: runs.length, summary }, null, 2));
if (opt.md) console.log(`written: ${opt.md}${opt.json ? ' and ' + opt.json : ''}`);
