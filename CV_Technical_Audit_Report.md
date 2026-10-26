# Code-Grounded Technical Audit of the `Shayan-Amz` GitHub Portfolio
### For upgrading the Academic CV of Shayan Amouzadeh (M.Sc./M.A.Sc./M.Eng. applications, Canada)

**Audit date:** 2026-10-26 · **Auditor role:** Senior Systems/AI Engineer + Canadian CS Grad-Admissions Reviewer
**Method:** every repository under `github.com/Shayan-Amz` was cloned at HEAD; source, build scripts, CI workflows and tests were read directly. Where a build toolchain was available in the sandbox, the test suites were **compiled and executed** so that the numbers below are observed, not quoted. Items marked ⚠️ are claims found in the existing CV draft / portfolio site that the code does **not** support and must be corrected before submission.

---

## Step 1 — Complete Repository Inventory

`gh api user` authenticated as `Shayan-Amz`; `gh repo list --visibility private` returned **0 private repositories**. All 11 repositories are public.

| # | Repository (URL) | Visibility | Primary language(s) | Active source LOC¹ | Commits | CI/CD (`.github/workflows`) | Last CI run |
|---|---|---|---|---|---|---|---|
| 1 | [Real-Estate-File-Manager-Project](https://github.com/Shayan-Amz/Real-Estate-File-Manager-Project) | Public | PHP, JavaScript, HTML/CSS, Python (tests) | **9,878** (+12,165 in recovery/defense snapshots) | 79 | ❌ none (tests run locally: `unittest`, `node --test`, Puppeteer) | — |
| 2 | [OpenGL-Dream-Village](https://github.com/Shayan-Amz/OpenGL-Dream-Village) | Public | C++17, C99 | **5,602** (+1,992 legacy) | 21 | ✅ `ci.yml` – Ubuntu/GCC, macOS/Clang, Windows/MSVC (MSBuild + CMake) | success 2026-09-19 |
| 3 | [World-Cup-Simulator-And-Analyzer](https://github.com/Shayan-Amz/World-Cup-Simulator-And-Analyzer) | Public | JavaScript (ES2017), PHP 8, SQL, CSS | **4,152** | 7 | ❌ none (Dockerfile + docker-compose provided) | — |
| 4 | [Shayan-Amz.github.io](https://github.com/Shayan-Amz/Shayan-Amz.github.io) | Public | HTML/JS (single file, Tailwind, i18n fa/en) | **3,539** | 15 | ❌ | — |
| 5 | [Floating-Point-ALU](https://github.com/Shayan-Amz/Floating-Point-ALU) | Public | C++17 (header-only) | **1,012** (+70 legacy) | 12 | ✅ `ci.yml` – 4-way matrix: ubuntu/gcc, ubuntu/clang, macos/clang, windows/msvc | success 2026-09-19 |
| 6 | [Fractional-Knapsack-Greedy](https://github.com/Shayan-Amz/Fractional-Knapsack-Greedy) | Public | C++17 (header-only), Python (plot) | **680** | 9 | ✅ `ci.yml` – same 4-way OS/compiler matrix | success 2026-09-19 |
| 7 | [Movie-ML-Pipeline](https://github.com/Shayan-Amz/Movie-ML-Pipeline) | Public | Python 3.10+ | **665** | 17 | ✅ `ci.yml` – Python 3.10 & 3.12, `ruff check`, `pytest` | success 2026-09-17 |
| 8 | [ARM-Assembly-Flag-Renderer](https://github.com/Shayan-Amz/ARM-Assembly-Flag-Renderer) | Public | ARMv7-A GNU assembly, Python (Unicorn harness) | **413** (+44 legacy) | 8 | ✅ `ci.yml` – matrix {gnu binutils, zig cc}; emulate + verify + artifact upload | success 2026-09-19 |
| 9 | [Unity-School-Directory-UI](https://github.com/Shayan-Amz/Unity-School-Directory-UI) | Public | C# (Unity 6000.0.41f1) | **149** (3 scripts) | 3 | ❌ | — |
| 10 | [Shayan-Amz](https://github.com/Shayan-Amz/Shayan-Amz) | Public | Markdown (profile README) + CV docx/pdf/xlsx | — | 1 | ❌ | — |
| 11 | [Ai-Learning](https://github.com/Shayan-Amz/Ai-Learning) | Public | none (one `.docx`) | 0 | 2 | ❌ | — |

¹ LOC = `wc -l` over `.cpp .hpp .h .c .py .php .js .cjs .html .css .sql .s .cs .yml CMakeLists Makefile .ld .toml`, excluding `third_party/`, build outputs, and verbatim legacy/recovery copies (reported separately).

**Repo 11 note:** `Ai-Learning` contains only a Persian petroleum-engineering internship report (Damavand Energy Asaluyeh, water treatment/MED/DM). It has no code and no relation to CS; it should **not** appear on the CV and ideally should be removed/archived before reviewers browse the account.

### Portfolio site (`shayan-amz.github.io`) — parsed content
Single `index.html` (2,755 code lines) with a bilingual `i18n` object and an inline `projects[]` array (8 cards: Amlak-e-Man, Movie-ML, World-Cup, FP-ALU, OpenGL, Unity, Knapsack, ARM) plus a printable CV section. Stats banner: "8+ projects · 2+ yrs · AI & NLP · 6+ langs". The Amlak-e-Man card lists metrics **"85 %↓ bandwidth", "90 %+↓ image size", "320 ms avg latency", "96 % AI extraction accuracy", "92 % ASR"** and mentions "Llama-3", "JWT (RFC 7519)", "Spatial Marker Clustering", "automated PDF catalog", "Collaborative Filtering" (Movie) and "Dijkstra / Towers of Hanoi" (Knapsack). **See §4 — several of these are not supported by the code.**

---

## Step 2 — Deep Codebase Extraction per Project

### 1. Intelligent Real-Estate CRM Platform — *Amlak-e-Man* (B.Sc. capstone, live at amlak-e-man.ir)
**Repo:** `Shayan-Amz/Real-Estate-File-Manager-Project` · Public · 79 commits (2026-09-05 → 09-19)

**Tech stack (verified from files):** PHP ≥ 7.4 (`api.php` 1,103 lines, `stt.php` 293, `setup_db.php`, `backup.php`, `tools/health_check.php` 566), MySQL 5.7+/MariaDB via **PDO** (`ERRMODE_EXCEPTION`, `utf8mb4`), GD image library, cURL; frontend = one `index.html` (4,688 lines, vanilla JS, inline CSS, RTL, Vazirmatn font), `sw.js` service worker, `manifest.json`; **Neshan Leaflet SDK v1.0.8 on Leaflet 1.9.4** (`static.neshan.org/sdk/leaflet/v1.9.4/neshan-sdk/v1.0.8`), Chart.js; external AI: **OpenRouter** chat-completions, **Hugging Face Inference Router / Groq / OpenAI Whisper**. Zero Composer/npm dependencies, no build step (shared-hosting target, Apache `.htaccess`). Tests: Python `unittest` (SQLite fixtures), Node `node --test`, Puppeteer-core + @sparticuz/chromium.

**Code-verified quantitative metrics**
| Metric | Value (source) |
|---|---|
| API action handlers in `api.php` | **17** (`getData, ping, transcribe_audio, jarvisProcess, changeMyPassword, resetMemberPassword, saveAgency, loginManager, loginConsultant, getNotes, saveNotes, saveMember, saveProperty, saveDemand, deleteProperty, deleteDemand, deleteMember`) |
| MySQL tables | **7** – `agencies, properties, demands, members, rate_limits, personal_notes, sys_config` (`properties` has 38 columns in the INSERT list) |
| Indexes created by runtime migration | **4** – `members(agencyId,name)`, `properties(agencyId)`, `properties(status,showToGuest)`, `demands(agencyId)` + `UNIQUE personal_notes(agencyId,username)`; `SCHEMA_VERSION = 6` gate |
| Prepared statements / UPSERTs | all data access via `prepare()/execute()`; **7** `INSERT … ON DUPLICATE KEY UPDATE` statements; **no explicit transactions** (`beginTransaction` count = 0) |
| Token lifetime | `time() + 108000` s = **30 h** |
| Rate limit | **150 req / 60 s** per key `substr(sha256(ip|agencyId|token),0,15)`; probabilistic GC (`random_int(1,20)===1`) of rows older than 300 s; fail-open on DB error |
| Image pipeline limits | client canvas ≤ 800 px, JPEG q=0.7, max **3 images**, 10 MB pre-check; server: `MAX_IMAGE_B64_CHARS`, `getimagesizefromstring` pixel-bomb guard (`MAX_IMAGE_PIXELS`), GD resample ≤ 800 px, `imagejpeg(…,70)`, SVG/XML payloads rejected |
| STT limits | `STT_MAX_BYTES` = 8 MiB, `STT_TIMEOUT` 45 s, connect 10 s, `STT_LANGUAGE='fa'`, recording cap 60 s, resample to **16 kHz mono PCM-16 WAV** |
| LLM extraction contract | **26-field allow-list** in `$allowed[]`, system prompt `jarvis-prompt30.txt` = **16 numbered rules** + 2 worked examples, `response_format: json_object`, ≤ 3 attempts |
| UI filter controls | **20** `filter-*` inputs (10 agency + 10 guest: usage, deal type, status, min/max area, min/max price, min/max rent, exchange, partner, pre-sale) |
| Polling | `fetchAllData` every **15 s** with delta-sync header; heartbeat `sendPing` every **20 s** |
| Automated tests | **47** assertions-level tests: 9 Python (`test_get_data_scope.py`, SQL-scope against SQLite), 13 `jarvis30.fields.test.cjs`, 5 `recovery29.worker.test.cjs`, 13 `academic/tests/metrics.test.cjs`, 7 `ui.test.cjs`; plus 10 headless-Chromium startup checks (`recovery29.browser.cjs`) and a PHP contract test |

**Architecture & algorithms (exact names)**
- **Routing / validation:** single front-controller `api.php?action=…`; `OPTIONS` pre-flight; CORS allow-list computed from `ALLOWED_ORIGIN` (same-origin default); CSP header; gzip via `ob_gzhandler`; global `set_exception_handler` that logs and returns a generic 500 (no stack leakage). Body is JSON-decoded then recursively `sanitizeInput()` (`strip_tags` + `htmlspecialchars(ENT_QUOTES)`), skipping credential keys and `data:image` payloads. A static `api_key` gate + role matrix: public actions `{loginManager, loginConsultant, saveAgency, getData}`; guest-forbidden set of 8 mutating actions; manager-only deletes.
- **Authentication (custom, not JWT in production):** `generateSecureToken($agency,$role,$name,$salt,$plan)` → `base64(json{a,r,n,p,exp}) . hash_hmac('sha256', payload, APP_SALT)`. Verification: `hash_equals()` constant-time compare → `exp` check → **tenant binding** (`token.a === X-Agency-ID` header) → for consultants a live DB status check (`members.status === 'active'`) so blocked accounts are revoked immediately. PINs: `pin_matches()` supports bcrypt (`password_verify`) and legacy plaintext via `hash_equals`; system-owner password only via `MASTER_PASSWORD_HASH` (bcrypt). `getRealIp()` trusts `CF-Connecting-IP`/`X-Forwarded-For` only when `TRUST_PROXY_HEADER` is on (anti-spoofing of rate-limit key). Guest responses mask agency IDs as `'ag_'.substr(sha256(id.APP_SALT),0,8)` (anti-IDOR). `safeUploadRelPath()` regex-whitelists `uploads/<name>.(jpg|jpeg|png|webp|gif)` and rejects `..`/separators (path-traversal fix). Uploads dir gets an auto-written `.htaccess` disabling script execution.
- **Delta synchronisation:** client sends `X-Data-Hash`; server compares with `sys_config.last_update` (`UNIX_TIMESTAMP()` bumped by `markSystemUpdated()`) and answers `{unmodified:true}` on a hit — a change-token short-circuit, not a byte-level diff.
- **Multi-tenancy & RBAC:** 3 roles (مدیر/manager, مشاور/consultant, مهمان/guest) × 3 plans (`Basic/Pro/VIP`, carried in the token as `p`); VIP gate on `transcribe_audio` and `jarvisProcess`; per-row visibility flags `showToGuest/showPriceGuest/showImagesGuest` enforced server-side.
- **"Jarvis" NLP pipeline (`jarvisProcess`):** text → OpenRouter `POST /api/v1/chat/completions` with `provider.allow_fallbacks=true`, model from `OPENROUTER_MODEL` (default **`google/gemma-4-26b-a4b-it:free`**; code rejects IDs without `provider/` prefix), system prompt = Persian extraction contract (`usage` enum of 6, `dealType` enum of 3, Toman normalisation incl. ریال÷10, `pricePerMeter` vs `price`, null-on-ambiguity, anti-prompt-injection clause). Retry ladder: `[endpoint+json_object, endpoint−json_object]` capped at 3, abort on 401/402, 10 s connect / 45 s total, TLS verify on. Response is fence-stripped, JSON-decoded, **schema-checked (`params` must be object), whitelisted to 26 fields, coerced to scalars**; identity/tenant/status/image/publication fields can never be set by the model. Client-side `jarvis/fields30.js` `normalize()` re-validates (bounded `quantity()`, Persian/Arabic digit folding, spoken-number parsing e.g. "هزار و چهارصد و دو"→1402, phone E.164→`0XXXXXXXXXX`, enum aliasing, derived `price = pricePerMeter × area` only for explicit sale, conflict warnings) and opens a **pre-filled property modal for human review** — no auto-commit.
- **Whisper STT (`transcribe_audio` → `stt.php`):** browser `navigator.mediaDevices.getUserMedia({audio:true})` → `MediaRecorder` (WebM/Opus) → `AudioContext.decodeAudioData` → `encodeWavPcm16()` (channel-average to mono, resample to 16 kHz, RIFF/WAVE header built in a `DataView`) → `FormData` multipart `audio_file` → `stt_validate_upload()` (`is_uploaded_file`, size, `UPLOAD_ERR_*` mapping) → provider switch `stt_transcribe()`: `hf` → `router.huggingface.co/hf-inference/models/openai/whisper-large-v3` (raw bytes, MIME from `stt_mime_for()`), `groq` → `api.groq.com/openai/v1/audio/transcriptions` model `whisper-large-v3-turbo`, `openai` → `whisper-1` (both via `CURLFile`); unified `['ok','text','error','provider']` result; transcript is then fed to `jarvisProcess`.
- **Demand↔property matching (client, `index.html` ≈ l.2972):** filter `status==='موجود'`, same `usage` & `dealType`, bidirectional substring city match after `normalizeText()`, **area within ±15 %**, budget rule by deal type (`price ≤ 1.10×budget` | `deposit ≤ 1.10×deposit` | both deposit & rent ≤ 1.10×) — O(P) per demand.
- **PWA / Service Worker (`sw.js`):** `skipWaiting` + `clients.claim`; on activate deletes only caches prefixed `amlak-safe-cache-`; fetch handler is **network-only**, bypasses `api.php`/non-GET, forces `cache:'no-store'` for navigations/scripts/styles, and returns a 503 diagnostic HTML page offline (deliberately never serves stale HTML for failed JS — unit-tested).
- **Geo & catalog:** lazy-loaded Neshan SDK (`loadMap()` with 60 s retry back-off), `L.Map` with `maptype:'dreamy'`, draggable `L.marker` + click → writes `geo-lat/geo-lng`; main map renders one marker per property; card deep-links to `neshan.org/maps/search/lat,lng` for routing. **Catalog export = `window.print()` + two `@media print` stylesheets** (no PDF library). CSV export uses a UTF-8 BOM (`\uFEFF`) and `text/csv` blob. Date conversion via `Intl.DateTimeFormat('fa-IR-u-nu-latn')` (Jalali).
- **Image watermarking (client):** canvas resize to ≤ 800 px, `ctx.rotate(-π/4)`, agency-name text at `w/12` px, `rgba(255,255,255,.4)` + shadow, `toDataURL('image/jpeg',0.7)`.
- **Thesis evaluation tooling (`academic/`):** separate HS256 **JWT (RFC 7519/7518) implementation `Jwt.php`** (issuer/audience/leeway checks, header allow-list) for the evaluation console; `metrics.js` implements **WER (Levenshtein on NFKC-normalised Persian), per-field precision/recall/F1, type-compliance errors, p50/p95 latency**; `cases.json` holds **5 gold scenarios (C01–C05)**. The report (`academic/report/01-source-audit.fa.md`) explicitly states accuracy/latency numbers are withheld until real runs are recorded — **so no measured accuracy exists in the repo**.

**3 CV bullets (code-verified)**
- Architected and deployed a production multi-tenant real-estate CRM (PHP/PDO + MySQL, 7-table schema, 17-action REST front controller, zero-dependency 4.7 k-line vanilla-JS PWA) with runtime schema migration (`SCHEMA_VERSION`-gated DDL + 4 composite indexes) and a change-token delta-sync protocol (`X-Data-Hash` vs `sys_config.last_update`) polled every 15 s.
- Engineered a defence-in-depth auth layer: HMAC-SHA256 signed, tenant-bound 30-hour tokens verified with constant-time `hash_equals`, per-request consultant revocation, bcrypt/`password_verify`, SHA-256 agency-ID masking against IDOR, regex-whitelisted upload paths, pixel-bomb and SVG rejection in the GD image pipeline, and a 150 req/min sliding-window rate limiter keyed on SHA-256(IP‖tenant‖token).
- Built the "Jarvis" voice-to-form pipeline: browser `MediaRecorder` → custom 16 kHz PCM-16 WAV encoder → provider-switchable Whisper-large-v3 (HF/Groq/OpenAI) → OpenRouter LLM with a 16-rule Persian JSON-extraction prompt and `json_object` mode → server-side 26-field allow-list + client-side normaliser (Persian numerals, spoken numbers, Toman/Rial units), covered by 47 automated tests and an offline WER/F1 evaluation harness.

---

### 2. IEEE 754 Floating-Point ALU
**Repo:** `Shayan-Amz/Floating-Point-ALU` · Public · 12 commits

**Tech stack:** C++17 header-only (`include/fp32/fp32.hpp`, 355 lines), CMake ≥ 3.14 + Makefile fallback, `.clang-format`; CLI `fp32calc` (`src/main.cpp`), test binary `test_fp32`, tool `legacy_accuracy`, `tools/plot_accuracy.py`. Warnings: `-Wall -Wextra -Wpedantic -Wshadow -Wconversion -Wsign-conversion` / `/W4 /permissive-`; tests built with **`-frounding-math`** (GCC/Clang) or **`/fp:strict`** (MSVC) so `fesetround()` is honoured.

**Bit-width / standard:** **binary32 (single precision) only** — constants `kFractionBits=23, kExponentBits=8, kBias=127`. No binary64, no FMA, no sqrt, no comparison/conversion ops beyond `from_float/to_float/from_binary_string/to_binary_string`. ⚠️ CV must say "single-precision adder/multiplier/divider", not generic "ALU with all operations".

**Operations & algorithms (function names):**
- `add` / `sub` (≡ `add(a, negate(b))`): operand ordering so |x|≥|y| (sign of larger), 3-bit GRS widening, `shift_right_sticky()` alignment (OR-reduction of discarded bits), magnitude add/sub, carry-out right-shift or leading-one left-normalisation **bounded at exponent 1** (gradual underflow falls out naturally), exact-cancellation → signed zero by rounding mode.
- `mul`: `detail::normalize()` subnormal operands, 24×24 → 48-bit `uint64_t` product, leading-one at bit 46/47 detection, denormalisation shift when exponent < 1.
- `div`: dividend doubling to keep quotient in [1,2), **integer long division producing 27 quotient bits** (`dividend << 26 / y.significand`), non-zero remainder → sticky.
- `detail::round_and_pack()`: GRS layout (bit 26 leading, bits 25..3 fraction, guard/round/sticky), 1.111…→10.000 carry fix-up, subnormal/zero packing, `overflow()` per IEEE 754 §7.4 (±∞ or ±MaxFinite depending on direction).
- Whole datapath is `constexpr` (`static_assert(div(1.0f,3.0f bits) == 0x3EAAAAAB)` compiles).

**Rounding & special cases explicitly handled:** `enum class Rounding {NearestEven, TowardZero, TowardPositive, TowardNegative}` — all **4** IEEE 754 directions; ±0 (sign rules for 0+0 and x−x per mode), ±∞, **quiet & signalling NaN** (`propagate_nan` keeps first NaN payload and sets `kQuietBit`; `kDefaultNaN = 0x7FC00000` for ∞−∞, 0×∞, 0/0, ∞/∞), subnormals as inputs and outputs, overflow saturation vs ∞, underflow to zero with tie-to-even (tested: `min_subnormal×0.5 → +0`, `3·min_sub×0.5 → 2·min_sub`).

**Verification (executed in this audit, `./test_fp32 250000`):**
- Hand-picked: 41×41 grid of edge values + 6 regression pairs × 4 ops × 4 modes = **26,992 checks, 0 failures**
- Random: 250,000 pairs × 8 operand families (any-bits, normal, near-one, tiny, huge, subnormal×normal, huge÷tiny, near-cancelling) × 16 = **32,000,000 checks, 0 failures**
- 15 property checks + 2 compile-time `static_assert`s — **total ≈ 32.03 M bit-exact differential checks vs. host FPU in 0.8 s**
- CTest targets: `conformance` (250 k) and `conformance_quick` (20 k); CI smoke-tests the CLI incl. `--trace` and `--mode down`.
- `legacy_accuracy` tool (run here): the original course adder was bit-exact on only **58.2 %** of 1.4 M random pairs (40.8 % off by 1 ulp, 1.1 % worse); the rewrite is **100 %**.

**CI:** 4-job matrix — `ubuntu-latest/gcc`, `ubuntu-latest/clang`, `macos-latest/clang`, `windows-latest/msvc`; `actions/checkout@v6`; Release builds; `ctest -R conformance$`.

**3 CV bullets**
- Implemented a bit-exact, `constexpr` C++17 software model of an IEEE 754 binary32 add/sub/mul/div datapath (unpack → align/multiply/long-divide → normalise → guard-round-sticky rounding → pack) supporting all four rounding modes, subnormals, signed zeros, ±∞ and quiet/signalling NaN propagation with integer arithmetic only.
- Verified correctness by differential testing against the host FPU under `fesetround()`: 32,026,992 operand-pair checks (41×41 edge grid + 8 stress distributions) with 0 mismatches, enforced on a 4-way GCC/Clang/AppleClang/MSVC CI matrix with `-frounding-math`/`/fp:strict`.
- Quantified the defects of the original course adder with a 1.4 M-sample accuracy harness (58.2 % exact, 40.8 % 1-ulp, 1.1 % >1-ulp errors) and eliminated them (100 % exact) by adding sticky-bit alignment, round-to-nearest-even and gradual-underflow handling.

---

### 3. Movie Recommender System
**Repo:** `Shayan-Amz/Movie-ML-Pipeline` · Public · 17 commits · https://github.com/Shayan-Amz/Movie-ML-Pipeline

**Tech stack (from `pyproject.toml`):** Python ≥ 3.10, `pandas>=2.0`, `beautifulsoup4>=4.12`, optional `streamlit>=1.30`; dev `pytest`, `ruff` (rules E,F,I,B,UP, line 120); src-layout package `movie_pipeline` (`extract.py`, `clean.py`, `recommend.py`), `app/streamlit_app.py`, notebook `02_data_cleaning.ipynb`. **No scikit-learn, NumPy-only-via-pandas, no TF-IDF, no cosine similarity, no collaborative filtering.** ⚠️

**Dataset (verified by loading `data/processed/all_years_movies_cleaned_ohe.csv`):** Iranian box-office archive scraped from 12 locally-saved Angular-rendered HTML pages (Solar-Hijri years **1392–1403 ≙ 2013–2024**); **686 films × 52 columns** = 9 base fields (`year,title,director,genres,rating,viewers,producer,total_sales,actors`) + **43 multi-label one-hot `genre_*` flags**; `rating` 1–5 (680 non-null), `total_sales` 8.4e4–3.24e11 (613 non-null), `viewers` ≤ 5,373 (549 non-null); **102 distinct genre signatures**.

**Pipeline (function names):**
- Stage 1 `extract.py`: `parse_archive_html()` with CSS selector `div.ng-star-inserted > app-movie-box-archive-desktop`, `parse_movie_card()`, `_labelled_value()` resolves Persian labels (تهیه کننده, کل فروش); `extract_all_years()` → CSV.
- Stage 2 `clean.py` `clean_movies()`: drop columns > 50 % missing (`MISSING_THRESHOLD`), strip text, `to_number()` strips Persian `٬`/comma thousands separators, `drop_duplicates()`, `one_hot_genres()` (set-based multi-label encoding, `split_genres()`), remove `RATING_OUTLIER == 10` artefact rows; CLI via `argparse`, `utf-8-sig` output.
- Stage 3 `recommend.py`: `add_genre_signature()` builds `_genre_sig` = `"-".join` of flags; `recommend_exact_combo(base_titles, df, top_k=5, n_required=3)` → boolean-mask candidates with identical signature (excluding seeds) → two **top-K rankings** (`sort_values('rating')`, `sort_values('total_sales')`). Content-based, exact-match, O(n) per query.
- UI: Streamlit app with `@st.cache_data` loader, sidebar metrics, `st.slider` for K ∈ [3,10], `st.multiselect` requiring exactly 3 seeds.

**Evaluation / tests:** no offline accuracy metric (no train/test split, no user data). **14 pytest tests** (5 clean, 3 extract, 6 recommend) — executed here: `14 passed in 0.32 s`. CI on Python 3.10 & 3.12 with ruff lint.

**3 CV bullets**
- Built an end-to-end, pip-installable data pipeline (BeautifulSoup → pandas → Streamlit) that scrapes 12 years (1392–1403 SH) of Iranian box-office archives into a 686-film dataset with 43 multi-label one-hot genre features and Persian-numeral normalisation.
- Designed a transparent content-based recommender (`recommend_exact_combo`) that matches exact 43-bit genre signatures (102 distinct combinations) and returns dual top-K rankings by critic rating and box-office revenue, served in a cached Streamlit UI.
- Enforced reproducibility with a src-layout package, pure-function cleaning stage mirrored from the exploratory notebook, 14 pytest unit tests and a ruff-linted GitHub Actions matrix on Python 3.10/3.12.

---

### 4. World Cup Tournament Simulator
**Repo:** `Shayan-Amz/World-Cup-Simulator-And-Analyzer` · Public · 7 commits · https://github.com/Shayan-Amz/World-Cup-Simulator-And-Analyzer

**Language(s):** ⚠️ **JavaScript (ES2017, `public/assets/js/dashboard.js` 1,390 lines) + PHP 8 (`php:8.3-apache` Docker image; `public/api/{auth,bootstrap,tournaments}.php`) + MySQL 8 / SQLite.** There is **no Python and no C++** — the CV draft's "Python / C++" must be corrected.

**Simulation engine `simulateMatch(team1, team2)`:**
- Dataset `ALL_COUNTRIES`: **178 national teams**, 6 confederations, integer `rating` ∈ **[46, 94]**, flag URLs (flagcdn).
- Outcome model: fixed draw probability **P(D)=0.25**; otherwise team-1 win with a **7-step function of rating gap Δ**: `w(Δ)=0.75 (Δ>20), 0.65 (10,20], 0.58 (5,10], 0.50 (−5,5], 0.42, 0.35, 0.25` ⇒ `P(W₁)=0.75·w(Δ)`.
- Scoreline sampling: categorical distributions — draws {0-0:40 %, 1-1:30 %, 2-2:30 %}; wins {1-0:35 %, 2-1:30 %, 2-0:20 %, 3-1:10 %, 3-0:5 %}; post-hoc perturbations: if |Δ|>15 stronger side +1 goal w.p. 0.3 and weaker −1 w.p. 0.2; random extra goal w.p. 0.1; goals clamped to [0,4]. (Not Poisson/Elo — a hand-tuned discrete stochastic model; README documents a 100,000-match Monte-Carlo characterisation figure.)
- Knockout `simulateKnockoutMatches()`: re-simulate on draw, after 3 attempts coin-flip "extra-time" goal.

**Data structures / architecture:**
- `selectedTeams[]` (exactly 16) → Fisher-Yates-style `sort(() => Math.random()-0.5)` shuffle → `tournamentGroups {A,B,C,D}` via `index % 4`; **round-robin** double loop `for i<n; for j=i+1<n` ⇒ 6 matches/group, 24 group + 4 QF + 2 SF + 1 F = **31 matches**.
- `teamStats[name] = {played,wins,draws,losses,gf,ga,gd,points}` via `updateTeamStats()`; **tie-break comparator: points → goal difference → goals for** (no head-to-head).
- Bracket: `runKnockoutStage()` seeds **A1–B2, C1–D2, B1–A2, D1–C2**, returns `{quarter,semi,final,champion}`; `renderBracket/createBracketRound` DOM renderer.
- Persistence: `tournaments(id, creation_date, champion, data JSON)` with indexes on `creation_date` and `champion`; REST `GET|POST|DELETE api/tournaments.php` (`list/get/save/delete_tournament`, PDO prepared, `ATTR_EMULATE_PREPARES=false`); `auth.php` with `password_verify`, `session_regenerate_id(true)`, `httponly`/`SameSite=Lax`/`secure` cookies; `require_auth()` guard. Dark/light theme (`initTheme`), history dropdown reload (`loadTournamentFromHistory`). Docker Compose (php-apache + mysql:8.0). No CI.

**3 CV bullets**
- Developed a full-stack 16-team World Cup simulator (vanilla JS SPA + PHP 8 REST API + MySQL/SQLite) over a 178-team rated dataset, running a round-robin group stage (24 matches) and a seeded 8-team knockout bracket (A1–B2, C1–D2, B1–A2, D1–C2) with points→goal-difference→goals-for tie-breaking.
- Designed a rating-driven stochastic match model: fixed 25 % draw prior, 7-tier win-probability step function over rating gap, categorical scoreline sampling (5 win / 3 draw outcomes) and asymmetric perturbations for |Δ|>15, characterised with a 100 k-match Monte-Carlo study.
- Implemented session-based authentication (bcrypt `password_verify`, `session_regenerate_id`, HttpOnly/SameSite cookies), PDO prepared statements with native prepares, JSON-document persistence of every simulated edition with denormalised champion indexing, and a reproducible Docker Compose deployment.

---

### 5. Classical Greedy Algorithms — Fractional Knapsack
**Repo:** `Shayan-Amz/Fractional-Knapsack-Greedy` · Public · 9 commits

⚠️ **The repository contains ONLY the fractional knapsack solver.** `grep -ri "dijkstra|hanoi|graph"` returns nothing. The CV/portfolio claims of "Dijkstra's Shortest Path" and "Towers of Hanoi" are unsupported — either add those implementations (with tests) or remove the claim.

**Tech stack:** C++17 header-only `include/knapsack/fractional.hpp` (119 lines), CMake 3.14 + Makefile, `.clang-format`, CLI `knapsack` (`src/main.cpp`, text/JSON output), `tests/test_fractional.cpp`, `bench/bench.cpp` + `bench/plot.py`; same 4-way OS/compiler CI matrix as the ALU (GCC, Clang, AppleClang, MSVC), CTest `unit_and_random` (20,000 rounds) + `cli_clrs` (regex `maximum value : 240`).

**Algorithms & complexity (verified in code):**
- `knapsack::solve()` — greedy by value density; `density_order()` uses `std::iota` + **`std::stable_sort` with a cross-product comparator** `v_a·w_b > v_b·w_a` (division-free, deterministic index tie-break) → **O(n log n) time, O(n) extra space**; returns `Solution{total_value,total_weight,fraction[],order[]}`; `validate()` throws `std::invalid_argument`.
- `zero_one_dp()` — 0/1 knapsack reference DP over integer weights, **O(n·W) time, O(W) space** (1-D rolling array).
- `fractional_upper_bound()` — LP-relaxation bound for branch-and-bound.
- README contains the **exchange-argument optimality proof**.

**Testing (executed here):** `./test_fractional 20000` → **328,582 checks, 0 failures**: hand-checked CLRS instance (value 240, fractions 1,1,⅔), README instance, zero-capacity/no-item edge cases, tie determinism, extreme-magnitude comparator, 3 exception paths; 20,000 random instances (n≤10) each checked for feasibility, ≤1 fractional item, capacity exhaustion, non-increasing density order, and **optimality vs. exhaustive vertex enumeration `brute_force()` (2ⁿ subsets × one fractional item)**, plus `fractional ≥ 0/1 DP` and integrality checks.
**Benchmark (executed here):** n = 20,000 → greedy **1.86 ms** vs 0/1 DP **26,382 ms** (~14,000×); mean integrality gap falls from 30.0 % (n=5) to 0.05 % (n=200) over 300 instances per size.

**3 CV bullets**
- Implemented a header-only C++17 greedy solver for the fractional knapsack problem in O(n log n) using a division-free cross-product density comparator with `std::stable_sort` for deterministic tie-breaking, accompanied by a written exchange-argument proof of optimality.
- Validated the solver with 328,582 automated checks — hand-derived CLRS instances plus 20,000 randomized instances compared against exhaustive LP-vertex enumeration and a 0/1 dynamic-programming reference — on a GCC/Clang/AppleClang/MSVC CI matrix.
- Benchmarked greedy vs. O(n·W) DP (1.9 ms vs. 26.4 s at n = 20,000) and measured the integrality gap (30 % → 0.05 % from n = 5 to 200), producing a reproducible CSV/plot pipeline.

---

### 6. Bare-Metal ARM Assembly VGA Renderer
**Repo:** `Shayan-Amz/ARM-Assembly-Flag-Renderer` · Public · 8 commits

**Target:** `.arch armv7-a`, `.cpu cortex-a9`, `.syntax unified`, ARM state — **Intel/Altera DE1-SoC Computer (Cortex-A9 HPS)** and the **CPUlator "ARMv7 DE1-SoC"** simulator; linker script `src/link.ld`; stack at `0x3FFFFFFC` (top of 1 GiB SDRAM).
**Framebuffer:** `PIXEL_BUFFER = 0xC8000000`, **320×240 visible, 16-bit RGB565** (`GREEN 0x07E0`, `WHITE 0xFFFF`, `RED 0xF800`), **row stride 1024 B** (`addr = base | y<<10 | x<<1`), 240 KiB span `0xC8000000–0xC803BFFF`.
**Algorithm:** `_start` walks a `.rodata` **data-driven stripe table** of `(colour, rows)` half-words and calls **AAPCS-conforming leaf routine `fill_rows(r0=dst, r1=colour, r2=rows) → r0=next row`**; `orr r1,r1,r1,lsl #16` packs **two pixels per 32-bit word**, inner loop `str r1,[r0],#4` × 160 per row, then `add r0,#384` skips the invisible pad; `subs/bne` loops; `b halt` spin. Uses only caller-saved r0–r3 (no stack spills).
**Toolchain/CI:** Makefile auto-selects `arm-none-eabi-as/ld/objcopy` or `zig cc -target arm-freestanding-eabi`; CI matrix `{gnu, zig}`, Python 3.12, `pip install unicorn`, uploads rendered PNG artifact.
**Verification harness `tools/emulate.py` (Unicorn engine; executed here):** hooks `UC_HOOK_CODE` + `UC_HOOK_MEM_WRITE` to count instructions, classify every store (visible / pad / out-of-bounds), detect the `b .` halt, and assert stripe geometry `--expect 80,80,80`. Result: **116,201 instructions, 38,400 word stores = 76,800 pixels, 0 pad writes, 0 out-of-bounds, halted, PASS**. Legacy course submission (kept in `legacy/Flag.s`): **353,286 instructions, 46,080 wasted pad writes, 9,216 out-of-bounds stores, stripes 84/80/76, no halt (executes data)** — a 3.04× instruction reduction and 3 correctness bugs fixed (incl. `0x0FE0` colour bit error).

**3 CV bullets**
- Wrote a bare-metal ARMv7-A (Cortex-A9/DE1-SoC) renderer that fills the memory-mapped 320×240 RGB565 VGA framebuffer at `0xC8000000` via an AAPCS-compliant leaf routine, packing two pixels per 32-bit store and honouring the 1024-byte row stride.
- Built a Unicorn-based emulation harness that instruments every instruction and memory write to verify stripe geometry (80/80/80 rows), bounds (0 out-of-range stores) and termination, run on CI with both GNU binutils and zig/clang cross-assemblers.
- Reduced executed instructions from 353,286 to 116,201 (−67 %) and eliminated 9,216 out-of-bounds writes and 46,080 redundant pad writes found in the original course submission through data-driven stripe tables and visible-width loop bounds.

---

### 7. Deterministic Graphics Pipeline — OpenGL Dream Village
**Repo:** `Shayan-Amz/OpenGL-Dream-Village` · Public · 21 commits · geometry attributed to krishnodey/Dream-Village (`NOTICE`)

Already-known highlights confirmed: `tools/softgl/softgl.c` (575 lines C99) half-space rasteriser citing Pineda SIGGRAPH '88; `-ffp-contract=off` added for GCC/Clang (comment documents the AppleClang-arm64 FMA failure mode); CTest `headless_render_matches_legacy --max-diff-ppm 0`; **day scene = 7,017 triangles / 1,248,754 fragments at 1300×650** (re-measured here).

**Additional verified highlights:**
- **Scene refactor:** `src/scene.h` defines `struct AnimationState` (train, bigBoat, smallBoats, `cloud[5]`, 2 birds, `orange[6]`, 2 planes, 2 diagonal birds, **`rain[12]` layers 10 units apart**), `enum class Scene {Day, Rain, Night, RainNight}`, pure `render(Scene, const AnimationState&)`, `advance()` tick, `setupProjection()` (100×100 orthographic). Scene compiled **twice** (system GL + softgl headers). `src/scene.cpp` = 1,640 lines, 36 drawing routines, 60 `glBegin` blocks.
- **Frame pacing:** `glutTimerFunc` at `kTickMillis = 33` (~30 Hz), keyboard `d/r/n/a` scenes, space = pause, `p` = PNG screenshot (`png_writer.cpp` via `stb_image_write`), `q` quit.
- **softgl scope:** **49 GL/GLUT entry points** implemented (matrix stacks depth 32, `glOrtho`, `glViewport`, `glRect*`, 9 primitive modes incl. `GL_POLYGON`/`GL_QUAD_STRIP` fan-triangulation, width-1 DDA lines with half-open endpoints and wide lines as 2 triangles, `glReadPixels` with `GL_PACK_ALIGNMENT`), **double-precision edge functions**, pixel-centre sampling (`x+0.5`), `owns_edge()` top-left fill rule, barycentric Gouraud interpolation, GL error tracking (`GL_INVALID_OPERATION` inside begin/end, `GL_INVALID_ENUM`).
- **Measured regression table (this run):** day 7,017 tri / 1,248,754 frag / 92.6 % coverage / **0 GL errors** (legacy raised **5**); rain 7,017 / 1,255,347 / legacy **605 errors**; night 6,989 / 1,219,474; rain_night 6,989 / 1,225,364 — **draw_diff = 0 pixels for all 4 scenes**; animation-advance diffs (6,555 / 4,320 / 11,456 px) confirm the state actually moves.
- **`softgl_selftest.c`:** 8 test functions, 28 assertions (shared-edge no-gap/no-overlap, fan/quad triangulation, Gouraud, matrix stack, lines, errors inside begin, readpixels round-trip).
- **CI:** 3 OS jobs; Windows job restores NuGet `nupengl.core`, builds `DreamVillage.sln` (VS2022 v143, x64 Release) with `-warnAsError`, then runs CMake head-less tests under MSVC; all jobs use `-DCMAKE_COMPILE_WARNING_AS_ERROR=ON`; frame PNGs uploaded as artifacts.

**3 CV bullets**
- Refactored a 2 k-line immediate-mode OpenGL 1.1 scene into an explicit `AnimationState` + pure `render()` function compiled against both system GL and a custom header set, enabling identical rendering on FreeGLUT (Windows/VS2022, Linux, macOS) and a GPU-less test harness.
- Authored `softgl`, a 575-line C99 deterministic software rasteriser implementing 49 GL/GLUT entry points — Pineda half-space edge functions in double precision, pixel-centre sampling, top-left fill rule, Gouraud interpolation, GL error semantics — with 28 self-test assertions.
- Established pixel-exact CI regression (`--max-diff-ppm 0`) across 4 scenes (up to 7,017 triangles / 1.26 M fragments at 1300×650) on GCC, AppleClang and MSVC, isolating and fixing an FMA-contraction non-determinism via `-ffp-contract=off` and eliminating 605 per-frame GL errors present in the legacy code.

---

### 8. Other Repositories
**Unity-School-Directory-UI** (`Shayan-Amz/Unity-School-Directory-UI`, Public): Unity **6000.0.41f1**, packages `com.unity.ugui 2.0.0`, `com.unity.inputsystem 1.13.1`, `com.unity.render-pipelines.universal 17.0.4` (URP 2D), `com.unity.feature.2d 2.0.1`, TextMeshPro. Three C# files (149 LOC): `[Serializable] Student{name,age,grade}`, `Teacher{name,age}`, `UIManager : MonoBehaviour` with `[Header]`-grouped inspector fields, tab switching (`ShowStudentsTab/ShowTeachersTab`, underline indicator re-parenting), prefab-instantiated list rendering (`PopulateStudentList/PopulateTeacherList`), live search (`FilterStudentList` via LINQ `Where`) and LINQ sorts (`OrderBy(name)`, `OrderByDescending(age/grade)`), wired through UnityEvents. Seed data: 3 students, 3 teachers. **No Entitas/ECS code exists in any public repository** — the CV's "Entitas ECS" claim refers to private employer work and cannot be evidenced on GitHub (state it as professional experience, not as a portfolio project).
**Compiler design / VLSI / FPGA / n8n / Selenium / ASP.NET Core / FastAPI:** no repositories exist. The profile README's "Enterprise REST API / CRM Core – ASP.NET Core / Clean Architecture", "Automation Pipeline & Web Scraper – Python & Selenium" and "Interactive Engine / OOP Framework – C#" entries are placeholders with no linked code and should be removed or backed by repos.

---

## Step 3 — Discrepancy Register (claims vs. code) — fix before submission

| Claim in CV draft / portfolio / README | Code reality | Recommended wording |
|---|---|---|
| "Fractional Knapsack, **Dijkstra**, **Towers of Hanoi**" suite | Only fractional knapsack exists | Drop Dijkstra/Hanoi or add them with tests |
| World Cup "Python / C++", "OOP" | Vanilla JS + PHP 8 + MySQL/SQLite | "JavaScript/PHP full-stack" |
| Movie recommender "Scikit-learn, cosine similarity, Content-Based **and Collaborative** Filtering" | pandas-only exact genre-signature content filter; no user data | "content-based exact-signature recommender (pandas)" |
| Real estate "**JWT (RFC 7519)**" | Production `api.php` uses a custom `base64(json).HMAC-SHA256` token; HS256 JWT exists only in `academic/` evaluation tool | "HMAC-SHA256 signed stateless tokens" (JWT only for the thesis evaluation console) |
| "Automated **PDF catalog generator**" | `window.print()` + `@media print` CSS | "print-optimised catalog view" |
| "**Llama-3** JSON extraction" | Default model `google/gemma-4-26b-a4b-it:free` via OpenRouter (configurable) | "OpenRouter-hosted LLM (configurable; Gemma by default)" |
| "85 % bandwidth ↓, 320 ms latency, 96 % extraction accuracy, 92 % ASR" | No measurement artifacts; `academic/report` explicitly withholds numbers pending real runs; evaluation harness has only 5 gold cases | Remove numbers or run the included WER/F1 harness and cite results |
| "Spatial Marker **Clustering**" | No clustering code (0 matches) | "interactive Neshan map with draggable geocoding marker" |
| "Atomic UPSERT **transactions**" | Single-statement `INSERT … ON DUPLICATE KEY UPDATE`; no `beginTransaction` | "idempotent UPSERT statements" |
| "Automated **SMS**" | Pre-filled `sms:` URI links only | "one-tap SMS/call deep links" |
| OpenGL "**3D** renderer with **lighting**" (portfolio) | 2D orthographic scene, no lighting | "2D animated scene; deterministic software rasteriser" |
| FP-ALU "complete ALU / IEEE 754" | binary32 add/sub/mul/div only | "single-precision add/sub/mul/div unit" |
| "Full-text search across 12+ filter criteria" | Client-side array filtering with 20 UI controls; no MySQL FULLTEXT index | "client-side multi-criteria filtering (20 controls)" |
| CV GPA "15.77" | `Review.docx` (same repo) states the correct GPA is **15.70** | Verify against transcript |

---

## Appendix — Reproduction log (commands executed in this audit)
```
Floating-Point-ALU      g++ -std=c++17 -O2 -frounding-math … tests/test_fp32.cpp && ./test_fp32 250000
                        → hand-picked 26992 / random 32000000 checks, 0 failures (0.80 s)
                        ./legacy_accuracy → legacy 58.2 % exact vs fp32::add 100 % (1.4 M pairs)
Fractional-Knapsack     ./test_fractional 20000 → 328582 checks, 0 failures; ./bench → n=20000: 1.86 ms vs 26381.8 ms
ARM-Flag-Renderer       make TOOLCHAIN=zig run → 116,201 insns, 38,400 stores, 0 OOB, PASS; make legacy → 353,286 insns, 9,216 OOB, FAIL
OpenGL-Dream-Village    cmake … -DDV_BUILD_APP=OFF && ctest → 2/2 passed; render_headless → 7017 tri / 1,248,754 frag / diff 0
Movie-ML-Pipeline       pytest -q → 14 passed; CSV → 686 rows × 52 cols, 43 genres, 102 signatures
gh run list (5 repos)   all latest CI runs: success
```
