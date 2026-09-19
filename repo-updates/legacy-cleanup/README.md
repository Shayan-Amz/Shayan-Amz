# Removing the left-over "legacy" material

The four READMEs no longer describe the changes: they describe the projects.  What is still in the
repositories is the material those old sections were built on — the earlier course submissions, the
defect tables and the comparison figures.

Two repositories keep their own earlier submission:

* **ARM-Assembly-Flag-Renderer** — `legacy/Flag.s` (an earlier 44-line course program),
  `legacy/README.md` (its defect table) and `docs/figures/before_after.png`.
* **Floating-Point-ALU** — `legacy/Project_Final.cpp`, `legacy/README.md`, `tools/legacy_accuracy.cpp`,
  `tools/plot_accuracy.py` and `docs/figures/legacy_vs_fp32.png`.

Deleting them is not just a delete: both the Makefile and the CI workflow build or run them, so those
files are updated here as well.  Everything in this folder has been built and tested locally with the
legacy material gone:

* ARM-Assembly-Flag-Renderer — `make TOOLCHAIN=zig all run figures` → `PASS`
  (80/80/80 rows, in bounds, halts), and the `gnu` recipe is unchanged.
* Floating-Point-ALU — `cmake -S . -B build && cmake --build build && ctest` → 2/2 pass,
  32 000 000 checks, 0 failures; `make && make test` → `ALL TESTS PASSED`.  GCC, zero warnings.

**OpenGL-Dream-Village keeps its `legacy/` folder on purpose.**  That folder is not an earlier
version of mine — it is the original program by Krishno Dey that the scene geometry comes from, and
it is what `NOTICE` refers to.  It is also the reference the `headless_render_matches_legacy` test
compares against, so removing it would remove the proof that the port draws the same pixels.  If it
still has to go, that is a larger change (the test and the README section that documents it), so ask
first.

## Files

| Repository | Replace with | Then delete |
| :--- | :--- | :--- |
| ARM-Assembly-Flag-Renderer | `ARM-Assembly-Flag-Renderer/Makefile`<br>`ARM-Assembly-Flag-Renderer/tools/emulate.py`<br>`ARM-Assembly-Flag-Renderer/.github/workflows/ci.yml` | `legacy/` (folder)<br>`docs/figures/before_after.png` |
| Floating-Point-ALU | `Floating-Point-ALU/CMakeLists.txt`<br>`Floating-Point-ALU/Makefile`<br>`Floating-Point-ALU/gitignore.txt` → `.gitignore` | `legacy/` (folder)<br>`tools/legacy_accuracy.cpp`<br>`tools/plot_accuracy.py`<br>`docs/figures/legacy_vs_fp32.png` |

Notes

* `Makefile`, `CMakeLists.txt` and `tools/emulate.py` are ordinary files: download them and drag them
  onto the right place in the repository (`emulate.py` goes **inside the `tools/` folder**).
* `.github/workflows/ci.yml` and `.gitignore` start with a dot, and drag & drop never uploads those
  (that is the same reason they were missing the first time).  Open the file in GitHub, use the
  pencil icon, select all, paste, commit — or use `github.dev` (press `.` on the repository page),
  which takes drag & drop for dot-files too.
* Deleting a *folder* is only possible in `github.dev` (press `.` on the repository page): right-click
  the folder → **Delete**, then Source Control → **Commit & Push**.  Single files can be deleted in
  the normal web UI as well.
* The `.gitignore` change only drops two ignore rules that referred to the tools being removed
  (`legacy_accuracy`, `accuracy.csv`); skipping it breaks nothing.
