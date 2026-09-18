# repo-updates (temporary — will be deleted at the end of the clean-up)

Ready-to-upload snapshots of the other repositories. Each ZIP contains the **complete new
content** of that repository: files that are not in the ZIP must be removed from the repo.

| Repository | Snapshot | Status |
| :--- | :--- | :--- |
| [Movie-ML-Pipeline](https://github.com/Shayan-Amz/Movie-ML-Pipeline) | [`Movie-ML-Pipeline.zip`](Movie-ML-Pipeline.zip) | ✅ uploaded & verified (CI green) — Description/Topics still to set |
| [RealStateHTML](https://github.com/Shayan-Amz/RealStateHTML) | [`RealStateHTML.zip`](RealStateHTML.zip) | ⏳ ready, not uploaded yet |
| [World-Cup-Simulator-And-Analyzer](https://github.com/Shayan-Amz/World-Cup-Simulator-And-Analyzer) | [`World-Cup-Simulator-And-Analyzer.zip`](World-Cup-Simulator-And-Analyzer.zip) | ✅ uploaded & verified |
| [Floating-Point-ALU](https://github.com/Shayan-Amz/Floating-Point-ALU) | [`Floating-Point-ALU.zip`](Floating-Point-ALU.zip) | ✅ uploaded & verified (CI green on 4 platforms) |
| [Fractional-Knapsack-Greedy](https://github.com/Shayan-Amz/Fractional-Knapsack-Greedy) (renamed) | [`Fractional-Knapsack-Greedy.zip`](Fractional-Knapsack-Greedy.zip) | ✅ uploaded & verified (CI green on 4 platforms) |
| [ARM-Assembly-Flag-Renderer](https://github.com/Shayan-Amz/ARM-Assembly-Flag-Renderer) (renamed) | [`ARM-Assembly-Flag-Renderer.zip`](ARM-Assembly-Flag-Renderer.zip) | ✅ uploaded & verified (CI green: gnu + zig) |
| [Unity-School-Directory-UI](https://github.com/Shayan-Amz/Unity-School-Directory-UI) (renamed) | [`Unity-School-Directory-UI.zip`](Unity-School-Directory-UI.zip) (delta) | ✅ uploaded & verified |
| [Cool-Computer-Graphics-Project-Using-Shapes](https://github.com/Shayan-Amz/Cool-Computer-Graphics-Project-Using-Shapes) → rename to **OpenGL-Dream-Village** | [`OpenGL-Dream-Village.zip`](OpenGL-Dream-Village.zip) | ⏳ ready, not uploaded yet |

---

## Option A — Git on your computer (recommended, keeps history)

```bash
git clone https://github.com/Shayan-Amz/<REPO>.git
cd <REPO>
git rm -r -q .                       # remove the old files from the repo
unzip -o ../<REPO>.zip -d .          # Windows PowerShell: Expand-Archive ..\<REPO>.zip -DestinationPath . -Force
git add -A
git commit -m "Restructure repository: documentation, tests, packaging"
git push origin main
```

> **Windows note:** `git rm -r .` and `Expand-Archive` work in PowerShell too. If `unzip` is not
> available, right-click the ZIP → *Extract All…* into the cloned folder and overwrite.

## Option B — GitHub web UI (no Git needed)

1. Open the repository on GitHub → delete the old files (each file → ⋯ → *Delete file* → commit).
   For `Movie-ML-Pipeline` that is: `download.py`, `extract.py`, `library`, `part_2.ipynb`, `part_3.py`,
   `all_years_movies_cleaned_ohe.csv` (it moves to `data/processed/`).
2. Extract the ZIP on your computer.
3. On GitHub → *Add file* → *Upload files* → drag the **contents** of the extracted folder
   (including the hidden `.github`, `.gitignore` files — enable "show hidden files" in your file manager).
4. Commit.

> Hidden files (`.github/`, `.gitignore`, `.editorconfig`, `public/.htaccess`) are **skipped by drag & drop**
> in the web UI. After uploading, create them by hand with *Add file → Create new file* (typing a path such
> as `.github/workflows/ci.yml` creates the folders) and paste the contents from the ZIP.

### Files to delete / create per repository

| Repository | Delete first | Create by hand after drag & drop |
| :--- | :--- | :--- |
| RealStateHTML | *(nothing — `index.html` is overwritten)* | `.gitignore`, `.editorconfig` |
| World-Cup-Simulator-And-Analyzer | `WorldCup.zip` (`README.md` is overwritten) | `.gitignore`, `public/.htaccess` |
| Floating-Point-ALU | `Project_Final.cpp` (it moves to `legacy/`; `README.md` is overwritten) | `.gitignore`, `.clang-format`, `.editorconfig`, `.github/workflows/ci.yml` |
| Fractional-Knapsack-Greedy | `Juice_Happiness.cpp` (`README.md` is overwritten) | `.gitignore`, `.clang-format`, `.editorconfig`, `.github/workflows/ci.yml` |
| ARM-Assembly-Flag-Renderer | `Flag.s` (it moves to `legacy/`; `README.md` is overwritten) | `.gitignore`, `.editorconfig`, `.github/workflows/ci.yml` |
| Unity-School-Directory-UI | nothing (`README.md`, `Assets/UIManager.cs`, `ProjectSettings/ProjectSettings.asset` are overwritten; `LICENSE` is new) | none |
| OpenGL-Dream-Village | the whole `Dream-Village-master/` folder, `Shapes.sln`, `Shapes.vcxproj`, `Shapes.vcxproj.filters` (`README.md`, `.gitignore`, `.gitattributes`, `packages.config` are overwritten). **v4 snapshot** — v3 plus: (a) the two CI failures fixed — MSVC's `/sdl` escalates the ported geometry's implicit `double`→`GLfloat` narrowing to *errors* (all 402 conversions are now explicit, pixels unchanged) and the arm64 macOS runners fuse multiply-adds, which broke the rasteriser self-test (`-ffp-contract=off` added), and (b) the pixel-buffer size in `src/main.cpp` made unsigned.  If you already uploaded v3, uploading **`src/scene.cpp`, `src/main.cpp`, `CMakeLists.txt`, `README.md`** is enough. — (a) MSVC error C4996 from the vendored `stb_image_write.h` fixed, (b) the real VS2022 screenshots you took replace the placeholder figure, and (c) CI now also runs on `master`.  Drag-and-drop never uploads dot-files, so the five of them have to be created by hand — see the dot-file list below. | `.gitignore`, `.gitattributes`, `.editorconfig`, `.clang-format`, `.github/workflows/ci.yml` |

---

## After uploading

For each repository also set (Settings → General, and the ⚙️ next to *About* on the repo page):

### Movie-ML-Pipeline
- **Description:** `End-to-end data pipeline for Iranian cinema (2013–2024): HTML scraping → pandas cleaning & multi-label genre encoding → Streamlit exact-genre recommender`
- **Topics:** `python` `pandas` `data-pipeline` `web-scraping` `beautifulsoup` `streamlit` `recommender-system` `data-cleaning` `iranian-cinema`
- The CI badge turns green automatically after the first push (GitHub Actions runs `ruff` + `pytest`).

### RealStateHTML
- **Description:** `Offline-first, dependency-free real-estate listing manager with a Persian RTL UI — filtering, sorting, localStorage persistence, sale / rent / full-deposit deal types`
- **Topics:** `javascript` `html5` `css3` `single-page-application` `localstorage` `rtl` `persian` `real-estate` `offline-first` `vanilla-js`
- Optional: **Settings → Pages → Deploy from branch `main` / (root)** gives you a live demo at
  `https://shayan-amz.github.io/RealStateHTML/` — add that link to the README and the About box.

### World-Cup-Simulator-And-Analyzer
- **Description:** `Full-stack World Cup simulator: rating-based stochastic match model, group & knockout stages in vanilla JS, PHP 8 REST API with session auth, MySQL/SQLite persistence of every simulated edition`
- **Topics:** `php` `javascript` `mysql` `sqlite` `rest-api` `simulation` `monte-carlo` `football` `world-cup` `tournament` `docker` `rtl` `persian`
- Demo login is `admin` / `admin123` (documented in the README); it is a bcrypt hash in `config/config.example.php`, not a plaintext password.

### Floating-Point-ALU
- **Description:** `Bit-exact software model of an IEEE 754 binary32 ALU in C++17 — add/sub/mul/div with guard-round-sticky rounding in all four modes, subnormals/Inf/NaN, differential tests against the host FPU`
- **Topics:** `cpp` `cpp17` `ieee754` `floating-point` `computer-arithmetic` `computer-architecture` `fpu` `header-only` `cmake` `simulation`
- The CI badge turns green after the first push (GitHub Actions builds with GCC, Clang, MSVC and on macOS and runs ~32 M bit-exact comparisons).

### Fractional-Knapsack-Greedy  (currently *Greedy-Algorithm-Project-Like-Fractional-Knapsack-Problem*)
- **Rename first:** Settings → General → Repository name → `Fractional-Knapsack-Greedy` (GitHub redirects the old URL; the profile README already points to the new name).
- **Description:** `Greedy O(n log n) solver for the fractional knapsack problem — header-only C++17, exchange-argument proof, randomized tests against exhaustive enumeration, 0/1 DP comparison and integrality-gap benchmark`
- **Topics:** `cpp` `cpp17` `algorithms` `greedy-algorithm` `knapsack-problem` `fractional-knapsack` `optimization` `linear-programming` `header-only` `cmake`

### ARM-Assembly-Flag-Renderer  (currently *Drawing-Flag-Assembly-Project*)
- **Rename first:** Settings → General → Repository name → `ARM-Assembly-Flag-Renderer`.
- **Description:** `Bare-metal ARMv7 assembly that draws the Iranian flag into the DE1-SoC VGA pixel buffer (RGB565) — AAPCS subroutine, data-driven stripes, Unicorn-based emulator harness that verifies geometry, memory bounds and termination in CI`
- **Topics:** `arm` `armv7` `assembly` `bare-metal` `de1-soc` `cpulator` `framebuffer` `vga` `rgb565` `unicorn-engine` `computer-architecture`
- CI assembles with both GNU binutils and zig and uploads the rendered frame as an artifact.

### Unity-School-Directory-UI  (currently *Unity_First*)
- **Rename first:** Settings → General → Repository name → `Unity-School-Directory-UI`.
- The ZIP is a *delta*: extract it and drag the four items (`README.md`, `LICENSE`, the `Assets` folder, the `ProjectSettings` folder) onto the repository root — GitHub merges them into the existing tree, nothing else is touched.
- **Description:** `Tabbed student/teacher directory built with Unity 6 uGUI + TextMeshPro — prefab-based list rendering, live search and LINQ sorting wired through UnityEvents (URP 2D, Input System)`
- **Topics:** `unity` `unity6` `csharp` `ugui` `textmeshpro` `urp` `linq` `ui` `game-development`

### OpenGL-Dream-Village
*(the repository is already renamed — the URL is https://github.com/Shayan-Amz/OpenGL-Dream-Village and the profile links to it)*

The drag & drop upload missed the dot-files (GitHub silently skips them) and pulled in the build output of your local run.  After the v3 upload:

1. **Delete** — in the repository root, remove
   - `Dream-Village-master/` (the old Code::Blocks sources — the same file is kept, verbatim, as `legacy/main.cpp`)
   - `Shapes.sln`, `Shapes.vcxproj`, `Shapes.vcxproj.filters`
   - `DreamVillage.vcxproj.user`
   - `packages/` (NuGet restore re-creates it: `packages.config` stays)
   - `x64/` and `DreamVillage/` (build output: `.obj`, `.pdb`, `.ilk`, `.tlog`, a copied `freeglut.dll`)
   - optionally the four `dream_village_*.png` in the root — their content already lives in `docs/figures/scenes_gpu.png`, which the README shows
2. **Upload** the v3 ZIP: extract it into an empty folder, select everything **except** the dot-files, drag it onto the repository root.  `README.md`, `packages.config`, `src/`, `tools/`, `legacy/`, `docs/`, `third_party/`, `CMakeLists.txt` and the `.sln`/`.vcxproj` are replaced; nothing else in the repository is touched.
3. **Create the five dot-files by hand** (Add file → Create new file — type the whole name, leading dot included; drag & drop cannot do this):
   `.gitignore` · `.gitattributes` · `.editorconfig` · `.clang-format` · `.github/workflows/ci.yml`
   — with exactly the content they have in the ZIP.  The workflow file is what turns CI on; without `.gitignore` the next `git add .` would commit `packages/`, `x64/` and the screenshots again.
4. **Settings → General → Description:**
   `Animated 2D village in immediate-mode OpenGL (C++17, FreeGLUT) — restructured into explicit animation state + pure render function, cross-platform CMake/VS2022 build, and pixel-exact regression tests on CI via a purpose-written software rasteriser. Geometry by krishnodey/Dream-Village (attributed).`
5. **Topics:** `opengl` `cpp` `cpp17` `computer-graphics` `freeglut` `2d-graphics` `software-rasterizer` `cmake` `visual-studio` `animation`
6. This repository's default branch is `master` (not `main`) — the workflow now triggers on both, so CI starts with the push that contains `.github/workflows/ci.yml`.  Three jobs: Ubuntu GCC, macOS Clang, and Windows MSVC (NuGet restore → `msbuild` with `-warnAsError` → CTest).
