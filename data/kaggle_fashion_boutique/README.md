# Kaggle Retail Fashion Boutique Data Sales Analytics 2025

- Source: https://www.kaggle.com/datasets/pratyushpuri/retail-fashion-boutique-data-sales-analytics-2025
- Type: Fashion retail operating KPI proxy
- Purpose in FitScope: Provides category KPI proxy fields such as price, rating, return flag, return reason, markdown and stock for operating readiness.
- Boundary: Use as company-KPI proxy until replaced by first-party internal data.

## File inventory

| File | Layer | Rows | Columns | What it is used for |
|---|---|---:|---:|---|
| [`kaggle_fashion_boutique_company_category_kpi.csv`](./processed/kaggle_fashion_boutique_company_category_kpi.csv) | `processed` | 6 | 14 | Dashboard-ready metric or sample table. |
| [`kaggle_fashion_boutique_daily_kpi.csv`](./processed/kaggle_fashion_boutique_daily_kpi.csv) | `processed` | 273 | 5 | Dashboard-ready metric or sample table. |
| [`kaggle_fashion_boutique_return_reason_metrics.csv`](./processed/kaggle_fashion_boutique_return_reason_metrics.csv) | `processed` | 36 | 4 | Dashboard-ready metric or sample table. |
| [`kaggle_fashion_boutique_dataset.csv`](./raw/kaggle_fashion_boutique_dataset.csv) | `raw` | 2,176 | 14 | Original source-shaped CSV. |

## Column lists

### `kaggle_fashion_boutique_company_category_kpi.csv`
`category`, `source_category`, `products`, `gmv`, `conversion`, `returnRate`, `margin`, `inventoryTurn`, `avg_rating`, `avg_markdown`, `returned_items`, `top_return_reason`, `size_issue_returns`, `quality_issue_returns`

### `kaggle_fashion_boutique_daily_kpi.csv`
`date`, `products`, `gmv`, `return_rate`, `avg_rating`

### `kaggle_fashion_boutique_return_reason_metrics.csv`
`category`, `return_reason`, `count`, `share_in_category`

### `kaggle_fashion_boutique_dataset.csv`
`product_id`, `category`, `brand`, `season`, `size`, `color`, `original_price`, `markdown_percentage`, `current_price`, `purchase_date`, `stock_quantity`, `customer_rating`, `is_returned`, `return_reason`

Full field explanations are in [`../COLUMN_DICTIONARY.md`](../COLUMN_DICTIONARY.md).
