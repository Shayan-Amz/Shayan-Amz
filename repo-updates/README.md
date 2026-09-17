# repo-updates (temporary)

Ready-to-upload snapshots of the other repositories, produced during the portfolio
clean-up session. Each ZIP is the **complete new content** of the repository
(including files that must be deleted — anything not in the ZIP should be removed).

| Repository | Snapshot | How to apply |
| :--- | :--- | :--- |
| `Movie-ML-Pipeline` | `Movie-ML-Pipeline.zip` | see below |

## How to apply a snapshot

```bash
git clone https://github.com/Shayan-Amz/<REPO>.git
cd <REPO>
git rm -r -q .                      # remove old files from the index and working tree
unzip -o ../<REPO>.zip -d .         # unpack the snapshot into the repo root
git add -A
git commit -m "Restructure repository (see README)"
git push origin main
```

This folder will be deleted at the end of the clean-up.
