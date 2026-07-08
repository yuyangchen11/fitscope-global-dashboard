# FitScope Commerce OS

FitScope Commerce OS is a role-based apparel commerce decision workspace. It connects public market signals, order operations, return pressure, fit feedback, and review evidence into a web dashboard for independent study research.

## Public Website

Share this GitHub Pages link with advisors or teammates:

https://yuyangchen11.github.io/fitscope-global-dashboard/

It works from any network and does not require the local computer to be running.

## Repository Map

| Folder | Purpose |
| --- | --- |
| `commerce-os/` | Main web dashboard, product notes, dashboard audit, role-based workspace specs. |
| `data/` | All source datasets and processed CSVs used by the dashboard. Each source has its own README. |
| `docs/` | Project structure and deployment notes for collaborators. |
| `supabase/` | Optional database/auth migration plan for a future backend. |
| `server.py` | Local demo server with lightweight login for manager/operator views. |

## Data Catalog

The data is intentionally committed as CSV instead of zip files so collaborators can preview, open, and trace the dashboard inputs directly.

Key documentation:

- [`data/README.md`](data/README.md): data-source inventory, file list, row counts, and usage notes.
- [`data/COLUMN_DICTIONARY.md`](data/COLUMN_DICTIONARY.md): every CSV column explained in plain language.
- [`docs/PROJECT_STRUCTURE.md`](docs/PROJECT_STRUCTURE.md): how the repo is organized.
- [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md): local and GitHub Pages deployment notes.

Current primary data sources:

| Source folder | Role in dashboard |
| --- | --- |
| `data/kaggle_olist/` | Real Brazilian ecommerce orders, order items, payments, reviews, sellers, customers, and product metadata. |
| `data/kaggle_hm_personalized/` | H&M apparel catalog and transaction structure for product/market views. |
| `data/ucsd_clothing_fit/` | Fit feedback and review evidence for sizing and body-type risk. |
| `data/kaggle_womens_reviews/` | Review benchmark and sentiment/rating evidence. |
| `data/kaggle_womens_sales/` | Boutique-style order-line sample used for SKU/order detail prototypes. |
| `data/kaggle_fashion_boutique/` | Boutique KPI, return reason, and daily operations sample. |
| `data/huggingface_hm_search/` | H&M-style search/sample metrics used as supplemental market structure data. |

## Local Development With Login

```bash
python3 server.py --port 4182
```

Then open:

```text
http://127.0.0.1:4182/commerce-os/index.html
```

The server creates `instance/fitscope.db` automatically and requires no third-party packages.

- Manager: `manager@fitscope.local` / `FitScope2026!`
- Operator: `operator@fitscope.local` / `FitScope2026!`

Set `FITSCOPE_DEMO_PASSWORD` before the first launch to change the initial demo password. Set `FITSCOPE_SECURE_COOKIE=1` when deploying behind HTTPS.

The localhost link only works on the computer running the local server. GitHub Pages remains a static preview and cannot provide secure database-backed login by itself.

## Dashboard Data Flow

The web page reads processed CSV files from `data/`. Olist raw files are stored in `data/kaggle_olist/raw`; `data/kaggle_olist/process_olist.py` rebuilds the processed dashboard tables. Dataset boundaries and unsupported metrics are documented in [`commerce-os/DATASET_CANDIDATES.md`](commerce-os/DATASET_CANDIDATES.md).

For the current independent study version, public datasets provide market and evidence signals. Company KPIs that do not exist in public data are either derived from available ecommerce order fields or clearly documented as modelled samples.
