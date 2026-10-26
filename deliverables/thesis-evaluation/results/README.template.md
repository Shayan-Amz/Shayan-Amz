# Results — Persian real-estate extraction benchmark (text track)

> Fill in by running (from `academic/evaluation/` after copying these files, or from this folder):
>
> ```bash
> OPENROUTER_API_KEY=sk-or-... node run_text_track.js --cases cases.v2.json --model google/gemma-4-26b-a4b-it:free --repeats 3 --out results/text-gemma.json
> node evaluate.js results/text-gemma.json --per-field --md results/README.md --json results/summary.json
> ```
>
> Commit `results/*.json` and `results/README.md`. The resulting numbers are what the CV may cite, e.g.
> "field-level micro-F1 = __._ % (exact-match __._ %, n = 50 × 3) with `<model>` on the amlak-fa-pilot-2 set".

## Provenance

| item | value |
|---|---|
| dataset | `cases.v2.json`, version `amlak-fa-pilot-2`, 50 cases (C01–C05 original, C06–C50 added 2026-10), gold labels reviewed by: ____ |
| prompt | `jarvis-prompt30.txt` (sha256: ____) — identical to `src/jarvis-prompt30.txt` of the app |
| model(s) | ____ via OpenRouter, `response_format=json_object`, provider fallbacks allowed |
| repeats | ____ per case (model is non-deterministic; report mean ± range across repeats if > 1) |
| date / machine | ____ |
| scorer | `metrics.js` (unchanged), `fieldScore` + `summarize` |
| excluded | nothing — failed calls are reported as failed runs, not dropped |

## Threats to validity (state these in the thesis / CV footnote)

* The gold labels were authored by the project author (single annotator); no inter-annotator agreement.
* 50 cases is a pilot-size set: a 95 % Wilson interval around an exact-match rate of 80 % at n = 50 is ≈ 67–89 %.
* The text track measures the LLM extraction only; the voice track (WER) needs real recordings via the browser tool.
* Free-tier OpenRouter routing may change the underlying model; `model_returned` is logged per run.
