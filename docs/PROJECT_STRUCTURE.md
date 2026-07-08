# Project Structure

FitScope Commerce OS is organized so a reviewer can separate product, frontend, backend prototype, and data assets quickly.

| Folder / file | Purpose |
|---|---|
| `commerce-os/` | Main dashboard website. `index.html` contains the current role-based Commerce OS frontend. |
| `data/` | Public and staged CSV datasets. Each source has its own folder with `raw/`, `processed/`, and `README.md`. |
| `data/README.md` | Data-source index with row counts, file counts, and source roles. |
| `data/COLUMN_DICTIONARY.md` | Field-level column dictionary for every CSV. |
| `dashboard/` | Earlier static dashboard prototype kept for design comparison. |
| `docs/` | Reviewer-facing project documentation and structure notes. |
| `server.py` | Local authenticated demo server. Creates SQLite runtime files under ignored `instance/`. |
| `supabase/` | Production-direction database/auth migration notes. |
| `README.md` | Main project entry, public URL, local run command, and data overview. |

## Data commit policy

- Commit public/anonymized CSV files that the dashboard or reviewers need.
- Do not commit runtime databases, `__pycache__`, local secrets, browser cache, or generated OS files.
- Keep processed CSV files unzipped so GitHub Pages and local static previews can load them.
- Move to Git LFS or external storage if any future raw file exceeds GitHub's 100MB single-file limit.
