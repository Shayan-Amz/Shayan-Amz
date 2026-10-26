# Hand-off Brief for the CV-Writing AI — Shayan Amouzadeh
*(Paste this entire file into the other AI's prompt. Everything below was verified against the actual source code, build files, CI workflows and test runs on 2026-10-26. Full evidence: `CV_Technical_Audit_Report.md`.)*

---

## INSTRUCTIONS TO THE CV WRITER

You are writing an academic CV for M.Sc./M.A.Sc./M.Eng. Computer Science / Computer Engineering applications in Canada (U of T, Waterloo, UBC, McGill, SFU).

**Rules:**
1. Use **only** the facts, numbers and names in this brief. Do not invent metrics, libraries, algorithms or technologies.
2. Every project bullet must follow: **Strong action verb + specific technical mechanism/algorithm + quantified, verifiable result.**
3. Each bullet ≤ 2 lines. 2–3 bullets per project. Lead with the strongest, most verifiable number.
4. Prefer concrete nouns (function/class/standard names) over marketing adjectives ("intelligent", "enterprise", "robust", "cutting-edge" are banned).
5. Every project gets its exact GitHub URL. Mention CI only where it exists (see table).
6. Apply every item in the **DELETE / CORRECT** list — those claims are not supported by the code and will be caught by a technical reviewer.
7. Order projects by academic weight: FP-ALU → OpenGL/softgl → Amlak-e-Man (thesis) → ARM renderer → Knapsack → Movie pipeline → World Cup → Unity.

---

## DELETE / CORRECT (claims that the code does NOT support)

| Current claim | Replace with |
|---|---|
| "Fractional Knapsack, **Dijkstra's Shortest Path, Towers of Hanoi**" | Only fractional knapsack exists. Delete Dijkstra and Hanoi. |
| World Cup simulator "**Python / C++**, OOP" | "JavaScript (ES2017) + PHP 8 + MySQL/SQLite full-stack" |
| Movie recommender "**Scikit-learn, NumPy, cosine similarity, Collaborative Filtering**" | "pandas content-based recommender using exact multi-label genre signatures" |
| Real estate "**JWT (RFC 7519)**" | "HMAC-SHA256-signed stateless tokens with tenant binding" (JWT exists only in the thesis evaluation tool) |
| "Automated **PDF catalog generator**" | "print-optimised catalog view (`@media print`)" |
| "**Llama-3**" / "Hugging Face & LLM APIs" | "OpenRouter-hosted LLM (configurable; Gemma by default) + Whisper-large-v3 via Hugging Face/Groq/OpenAI" |
| "**85 % bandwidth reduction, 320 ms latency, 96 % extraction accuracy, 92 % ASR**" | **Delete all four numbers.** No measurement exists in the repo. |
| "Spatial marker **clustering**", "automated **SMS**", "atomic **transactions**" | Delete. (Draggable Neshan marker; `sms:` deep links; single-statement UPSERT.) |
| "**Full-text search** across 12+ criteria" | "client-side multi-criteria filtering with 20 filter controls" |
| OpenGL "**3D** renderer with **lighting**" | "2D animated orthographic scene" |
| "IEEE 754 Floating-Point **ALU**" (implying full ALU / double precision) | "IEEE 754 **binary32** add/sub/mul/div unit" |
| "**Entitas ECS** project" in projects section | Keep only under *Experience* (SinSin Studio) — no public code exists. |
| "ASP.NET Core / Clean Architecture", "FastAPI", "Selenium scraper", "n8n", "VLSI/FPGA", "Compiler Design" as skills/projects | No repositories exist. Remove from Projects; list in Skills only if the applicant can defend them in an interview. |
| GPA **15.77** | `Review.docx` says **15.70** — confirm against transcript before use. |
| Repo `Ai-Learning` | Unrelated petroleum-engineering document — do not reference; owner should delete it. |

---

## ADD — Verified facts per project (use these numbers verbatim)

### 1. IEEE 754 binary32 Floating-Point Unit — https://github.com/Shayan-Amz/Floating-Point-ALU
- C++17, **header-only, fully `constexpr`**, integer arithmetic only (never touches host float registers).
- Ops: `add`, `sub`, `mul`, `div`. Datapath: unpack → align (sticky-bit right shift) / 24×24→48-bit multiply / 27-bit integer long division → normalise → **guard-round-sticky** rounding → pack.
- **All 4 IEEE 754 rounding modes** (nearest-even, toward-zero, +∞, −∞); subnormals (in & out), ±0 sign rules, ±∞, quiet/signalling NaN with payload propagation, default NaN `0x7FC00000`, overflow→∞/MaxFinite per mode.
- Verification: **32,026,992 bit-exact checks against the host FPU, 0 failures** (41×41 edge-value grid + 250,000 random pairs × 8 stress distributions × 4 ops × 4 modes), run in 0.8 s.
- Legacy course adder measured at **58.2 % bit-exact** on 1.4 M pairs (40.8 % off by 1 ulp); rewrite = 100 %.
- CI: GitHub Actions **4-way matrix — Ubuntu/GCC, Ubuntu/Clang, macOS/AppleClang, Windows/MSVC**; built with `-frounding-math` / `/fp:strict`; CMake + CTest + CLI smoke test. Warnings: `-Wall -Wextra -Wpedantic -Wshadow -Wconversion`.

**Ready bullets**
- Implemented a bit-exact, `constexpr` C++17 software model of an IEEE 754 binary32 add/sub/mul/div datapath (sticky-bit alignment, 48-bit product, 27-bit long division, guard-round-sticky rounding) supporting all four rounding modes, subnormals, signed zeros, ±∞ and NaN payload propagation using integer arithmetic only.
- Verified against the host FPU under `fesetround()` with 32,026,992 differential checks and 0 mismatches on a GCC/Clang/AppleClang/MSVC CI matrix.
- Quantified the original course adder at 58.2 % bit-exactness over 1.4 M samples and raised it to 100 % by adding sticky-bit alignment, round-to-nearest-even and gradual underflow.

### 2. OpenGL Dream Village + `softgl` deterministic rasteriser — https://github.com/Shayan-Amz/OpenGL-Dream-Village
- C++17 / OpenGL 1.1 / FreeGLUT; geometry attributed to krishnodey/Dream-Village (say "restructured", not "designed the art").
- Refactor: `struct AnimationState` (12 rain layers, 5 clouds, 6 falling fruit, train/boats/birds/planes), `enum class Scene {Day, Rain, Night, RainNight}`, pure `render(Scene, const AnimationState&)`, `advance()` tick at 33 ms (~30 Hz). Scene compiled twice (system GL + softgl headers).
- `softgl`: **575-line C99 software rasteriser, 49 GL/GLUT entry points**, Pineda (SIGGRAPH '88) half-space edge functions in double precision, pixel-centre sampling, top-left fill rule, barycentric Gouraud interpolation, DDA lines, GL error semantics; **28 self-test assertions**.
- Regression: **pixel-identical (0-pixel diff, `--max-diff-ppm 0`) to the legacy program across 4 scenes; day scene = 7,017 triangles / 1,248,754 fragments at 1300×650**, 92.6 % coverage; legacy raised **605 GL errors per frame** (rain scene) → 0.
- Determinism fix: `-ffp-contract=off` after diagnosing FMA contraction on AppleClang/arm64.
- CI: **Ubuntu/GCC, macOS/Clang, Windows/MSVC** (NuGet `nupengl.core` restore + `DreamVillage.sln` MSBuild `-warnAsError` + CMake head-less tests), `CMAKE_COMPILE_WARNING_AS_ERROR=ON`, PNG artifacts.

**Ready bullets**
- Restructured a 2 k-line immediate-mode OpenGL 1.1 scene into an explicit `AnimationState` + pure `render()` function compiled against both system GL and custom headers, enabling identical output on FreeGLUT (Windows/Linux/macOS) and a GPU-less test harness.
- Authored `softgl`, a 575-line C99 deterministic rasteriser (49 GL/GLUT entry points; Pineda half-space edge functions, pixel-centre sampling, top-left fill rule, Gouraud shading) with 28 self-test assertions.
- Established 0-pixel-difference CI regression across 4 scenes (7,017 triangles / 1.25 M fragments at 1300×650) on GCC, AppleClang and MSVC, fixing FMA-induced non-determinism with `-ffp-contract=off` and eliminating 605 per-frame GL errors.

### 3. Amlak-e-Man — Multi-tenant Real-Estate CRM (B.Sc. thesis, 19.50/20, live at https://amlak-e-man.ir) — https://github.com/Shayan-Amz/Real-Estate-File-Manager-Project
- Stack: PHP + **PDO/MySQL (7 tables, 4 composite indexes, 7 UPSERT statements, runtime `SCHEMA_VERSION`-gated migration)**, single-file 4.7 k-line vanilla-JS RTL PWA (service worker, manifest), GD image library, Neshan Leaflet SDK v1.0.8, Chart.js, Apache `.htaccess`; **zero Composer/npm dependencies**.
- API: single front controller `api.php?action=…` with **17 action handlers**; CORS allow-list, CSP header, gzip, recursive input sanitisation, role matrix (manager / consultant / guest) × plans (Basic / Pro / VIP).
- Security: **HMAC-SHA256 signed tokens** (`base64(json).hmac`, 30 h expiry, constant-time `hash_equals`, bound to `X-Agency-ID`, per-request consultant revocation); bcrypt `password_verify`; **150 req/min rate limiter keyed on SHA-256(IP‖tenant‖token)** with proxy-header trust flag; SHA-256 masking of agency IDs for guests (anti-IDOR); regex-whitelisted upload paths (path-traversal fix); pixel-bomb (`getimagesizefromstring`) and SVG rejection; script execution disabled in uploads dir.
- Sync: `X-Data-Hash` change-token vs `sys_config.last_update` → `{unmodified:true}` short-circuit, polled every 15 s; 20 s consultant heartbeat (`lastSeen`).
- Matching engine (client): same usage & deal type, normalised city match, **area ±15 %, budget/deposit/rent ≤ 110 %**.
- Images: canvas resize ≤ 800 px + −45° agency watermark + JPEG q0.7 client-side; GD re-encode ≤ 800 px q70 server-side; max 3 images.
- **Voice-to-form ("Jarvis")**: `MediaRecorder` → custom **16 kHz mono PCM-16 WAV encoder** → multipart upload (8 MiB cap, 45 s timeout) → provider-switchable **Whisper-large-v3 (Hugging Face) / whisper-large-v3-turbo (Groq) / whisper-1 (OpenAI)** → OpenRouter chat-completions with **`json_object` mode, 16-rule Persian extraction system prompt, 3-attempt fallback ladder** → **server-side 26-field allow-list** → client normaliser (Persian/Arabic digits, spoken numbers, Toman/Rial, phone formats, enum aliasing) → pre-filled form for human review (no auto-commit).
- Tests: **47 automated tests** (Python `unittest` SQL-scope on SQLite, Node `node --test`, 10 headless-Chromium startup checks) + offline **WER / per-field P-R-F1 / p95-latency evaluation harness** with 5 gold scenarios. No CI workflow.

**Ready bullets**
- Architected and deployed a production multi-tenant real-estate CRM (PHP/PDO + MySQL, 7-table schema with runtime versioned migration, 17-action REST front controller, zero-dependency 4.7 k-line vanilla-JS PWA) used by agencies via subscription tiers; graded 19.50/20 as B.Sc. thesis.
- Engineered a defence-in-depth auth layer — HMAC-SHA256 tenant-bound tokens with constant-time verification, bcrypt, SHA-256 ID masking against IDOR, whitelisted upload paths, image pixel-bomb/SVG rejection, and a 150 req/min rate limiter keyed on SHA-256(IP‖tenant‖token).
- Built a Whisper-to-LLM voice-entry pipeline (browser 16 kHz PCM-16 WAV encoder → Whisper-large-v3 via HF/Groq/OpenAI → OpenRouter LLM in JSON mode with a 16-rule Persian extraction prompt → 26-field server allow-list + client normaliser), covered by 47 automated tests and a WER/F1 evaluation harness.

### 4. Bare-metal ARM VGA Renderer — https://github.com/Shayan-Amz/ARM-Assembly-Flag-Renderer
- **ARMv7-A, Cortex-A9, DE1-SoC / CPUlator**; framebuffer `0xC8000000`, **320×240, 16-bit RGB565, 1024-byte row stride**; AAPCS leaf routine `fill_rows`, two pixels per 32-bit store, data-driven stripe table in `.rodata`.
- **Unicorn-engine harness** (hooks every instruction and memory write): **116,201 instructions, 38,400 stores, 0 out-of-bounds, halts cleanly** vs legacy course submission **353,286 instructions, 9,216 out-of-bounds stores, 46,080 wasted pad writes, wrong stripe heights (84/80/76), no halt**.
- CI: matrix **GNU binutils + zig/clang cross-assembler**, Python 3.12, PNG artifact upload. Makefile auto-detects toolchain.

**Ready bullets**
- Wrote a bare-metal ARMv7-A (Cortex-A9/DE1-SoC) renderer filling the memory-mapped 320×240 RGB565 framebuffer through an AAPCS-compliant leaf routine with two-pixels-per-word stores and stride-aware addressing.
- Built a Unicorn-based emulation harness verifying geometry, memory bounds and termination on CI with both GNU and zig/clang toolchains.
- Cut executed instructions by 67 % (353,286 → 116,201) and removed 9,216 out-of-bounds writes found in the original submission.

### 5. Fractional Knapsack (Greedy) — https://github.com/Shayan-Amz/Fractional-Knapsack-Greedy
- C++17 header-only; `std::stable_sort` with **division-free cross-product density comparator**; **O(n log n) time, O(n) space**; written **exchange-argument proof** in README; reference `zero_one_dp()` O(n·W).
- Tests: **328,582 checks, 0 failures** — CLRS instance, edge cases, **20,000 random instances vs exhaustive LP-vertex enumeration** and 0/1 DP.
- Benchmark: n = 20,000 → **1.86 ms greedy vs 26.4 s DP**; integrality gap 30 % (n=5) → 0.05 % (n=200).
- CI: same 4-way GCC/Clang/AppleClang/MSVC matrix, CTest + CLI smoke test.

**Ready bullets** — see audit report §5 (three bullets provided).

### 6. Movie data pipeline & recommender — https://github.com/Shayan-Amz/Movie-ML-Pipeline
- Python ≥ 3.10, **pandas, BeautifulSoup, Streamlit**; src-layout package; ruff-linted.
- Data: **686 Iranian films, 1392–1403 SH (2013–2024), 52 columns = 9 fields + 43 multi-label one-hot genres, 102 distinct genre signatures**; Persian thousands-separator normalisation; >50 %-missing column drop; rating-outlier removal.
- Recommender: exact genre-signature match → **dual top-K ranking by rating and by box-office** (K ∈ [3,10]); `@st.cache_data`.
- **14 pytest tests**; CI on **Python 3.10 & 3.12**.

### 7. World Cup Simulator — https://github.com/Shayan-Amz/World-Cup-Simulator-And-Analyzer
- **Vanilla JS + PHP 8.3 + MySQL 8 / SQLite**, Docker Compose; **178-team dataset (ratings 46–94)**; 16 teams → 4 groups round-robin (24 matches) → QF/SF/F seeded **A1–B2, C1–D2, B1–A2, D1–C2** (31 matches/edition).
- Match model: **25 % draw prior, 7-tier win-probability step function over rating gap, categorical scoreline sampling, perturbations for |Δ|>15**; 100 k-match Monte-Carlo characterisation figure.
- Tie-break: **points → goal difference → goals for**.
- Backend: PDO prepared statements (native prepares), `password_verify`, `session_regenerate_id`, HttpOnly/SameSite cookies, JSON-document persistence with indexed champion column. No CI.

### 8. Unity School Directory UI — https://github.com/Shayan-Amz/Unity-School-Directory-UI
- **Unity 6000.0.41f1, URP 17 (2D), uGUI 2.0, Input System 1.13, TextMeshPro**; `UIManager : MonoBehaviour`; prefab-instantiated lists, tab switching, **LINQ `Where`/`OrderBy` live search & sorting** via UnityEvents. (Minor project — one line in "Additional projects" is enough.)

---

## SKILLS SECTION (only code-evidenced items)
- **Languages:** C++17, C99, Python 3, PHP 8, JavaScript (ES2017), C# (Unity), ARMv7 Assembly, SQL, HTML/CSS
- **Systems & architecture:** IEEE 754 arithmetic, bit-level datapath modelling, memory-mapped I/O, AAPCS, bare-metal ARM, Unicorn emulation, `constexpr` metaprogramming
- **Graphics:** OpenGL 1.1 / FreeGLUT, software rasterisation (half-space edge functions, fill rules), deterministic floating-point builds
- **Algorithms:** greedy/exchange-argument proofs, dynamic programming, randomized differential testing, exhaustive-enumeration oracles
- **Data / ML:** pandas, BeautifulSoup, Streamlit, multi-label one-hot encoding, content-based recommendation; speech-to-text (Whisper via HF/Groq/OpenAI APIs), LLM structured extraction with JSON mode and prompt contracts, WER / precision-recall-F1 evaluation
- **Web & security:** PHP/PDO, MySQL/SQLite schema design and indexing, REST front controllers, HMAC-SHA256 tokens, bcrypt, rate limiting, CORS/CSP, PWA/service workers, Leaflet/Neshan maps
- **Build & CI:** CMake, Make, GitHub Actions cross-OS matrices (GCC/Clang/AppleClang/MSVC), CTest, pytest, ruff, node:test, Puppeteer, Docker Compose, MSBuild/NuGet, zig cross-compilation
- **Tools:** Git/GitHub, Plastic SCM, Visual Studio 2022, VS Code, CPUlator

## ONE-LINE RESEARCH-INTEREST FRAMING (evidence-backed)
"Computer architecture and systems programming (IEEE 754 arithmetic, bare-metal ARM), deterministic graphics and verification-driven software (pixel-exact CI, differential testing), and applied data/ML systems (speech-to-text + LLM structured extraction in a deployed product)."
