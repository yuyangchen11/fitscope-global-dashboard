# Kaggle Women Clothing Ecommerce Sales

- Source: https://www.kaggle.com/datasets/shilongzhuang/-women-clothing-ecommerce-sales-data
- Type: Order-style women clothing sales sample
- Purpose in FitScope: Provides SKU/order/date/size/color/price/quantity/revenue structure for order-detail and SKU drill-down design validation.
- Boundary: No native product-group taxonomy or returns.

## File inventory

| File | Layer | Rows | Columns | What it is used for |
|---|---|---:|---:|---|
| [`kaggle_womens_sales_daily_metrics.csv`](./processed/kaggle_womens_sales_daily_metrics.csv) | `processed` | 116 | 6 | Dashboard-ready metric or sample table. |
| [`kaggle_womens_sales_size_metrics.csv`](./processed/kaggle_womens_sales_size_metrics.csv) | `processed` | 10 | 5 | Dashboard-ready metric or sample table. |
| [`kaggle_womens_sales_sku_metrics.csv`](./processed/kaggle_womens_sales_sku_metrics.csv) | `processed` | 24 | 8 | Dashboard-ready metric or sample table. |
| [`kaggle_womens_sales_orders.csv`](./raw/kaggle_womens_sales_orders.csv) | `raw` | 527 | 8 | Original source-shaped CSV. |

## Column lists

### `kaggle_womens_sales_daily_metrics.csv`
`date`, `orders`, `line_items`, `units`, `revenue`, `avg_order_line_revenue`

### `kaggle_womens_sales_size_metrics.csv`
`size`, `line_items`, `units`, `revenue`, `share`

### `kaggle_womens_sales_sku_metrics.csv`
`sku`, `orders`, `line_items`, `units`, `revenue`, `avg_unit_price`, `top_size`, `size_missing_rate`

### `kaggle_womens_sales_orders.csv`
`order_id`, `order_date`, `sku`, `color`, `size`, `unit_price`, `quantity`, `revenue`

Full field explanations are in [`../COLUMN_DICTIONARY.md`](../COLUMN_DICTIONARY.md).
