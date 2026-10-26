#!/usr/bin/env bash
# One-shot: apply the citation/report commit to Floating-Point-ALU and create release v1.0.0.
# Run on your own machine where `git push` to Shayan-Amz/Floating-Point-ALU works and `gh auth status` is OK.
# Requires: Zenodo GitHub toggle for this repo already ON (done 2026-10-27).
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
WORK="${1:-$HOME/Floating-Point-ALU}"
if [ ! -d "$WORK/.git" ]; then git clone https://github.com/Shayan-Amz/Floating-Point-ALU "$WORK"; fi
cd "$WORK"
git checkout main && git pull --ff-only
git am --3way "$HERE/0001-add-citation-metadata-and-technical-report.patch"   # adds CITATION.cff, .zenodo.json, docs/technical-report.pdf, README section
git push origin main
gh release create v1.0.0 --repo Shayan-Amz/Floating-Point-ALU \
  --title "v1.0.0 — bit-exact binary32 ALU, 32M differential checks" \
  --notes "First archived release. Bit-exact IEEE 754 binary32 add/sub/mul/div (4 rounding modes, subnormals, NaN/Inf), constexpr datapath. 32,026,992 differential checks against the host FPU, 0 failures, on GCC/Clang/AppleClang/MSVC. Technical report: docs/technical-report.pdf."
echo "Done. In 2-5 minutes open https://zenodo.org/account/settings/github/ and copy the Concept DOI."
