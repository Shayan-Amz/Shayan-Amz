# repo-updates (temporary — will be deleted at the end of the clean-up)

Ready-to-upload snapshots of the other repositories. Each ZIP contains the **complete new
content** of that repository: files that are not in the ZIP must be removed from the repo.

| Repository | Snapshot | Status |
| :--- | :--- | :--- |
| [Movie-ML-Pipeline](https://github.com/Shayan-Amz/Movie-ML-Pipeline) | [`Movie-ML-Pipeline.zip`](Movie-ML-Pipeline.zip) | ✅ uploaded & verified (CI green) — Description/Topics still to set |
| [RealStateHTML](https://github.com/Shayan-Amz/RealStateHTML) | [`RealStateHTML.zip`](RealStateHTML.zip) | ⏳ ready, not uploaded yet |
| [World-Cup-Simulator-And-Analyzer](https://github.com/Shayan-Amz/World-Cup-Simulator-And-Analyzer) | [`World-Cup-Simulator-And-Analyzer.zip`](World-Cup-Simulator-And-Analyzer.zip) | ⏳ ready, not uploaded yet |

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
