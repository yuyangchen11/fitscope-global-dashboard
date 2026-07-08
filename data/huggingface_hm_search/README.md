# Hugging Face H&M Search / Sample Mirror

- Source: Derived from public H&M-style search/sample exports staged locally
- Type: Processed sample metrics
- Purpose in FitScope: Provides lightweight H&M-like processed metrics for fallback testing and dashboard development.
- Boundary: Not the primary audited source when Kaggle H&M files are available.

## File inventory

| File | Layer | Rows | Columns | What it is used for |
|---|---|---:|---:|---|
| [`huggingface_hm_search_articles_sample.csv`](./processed/huggingface_hm_search_articles_sample.csv) | `processed` | 1,000 | 25 | Dashboard-ready metric or sample table. |
| [`huggingface_hm_search_color_metrics.csv`](./processed/huggingface_hm_search_color_metrics.csv) | `processed` | 50 | 2 | Dashboard-ready metric or sample table. |
| [`huggingface_hm_search_index_group_metrics.csv`](./processed/huggingface_hm_search_index_group_metrics.csv) | `processed` | 5 | 2 | Dashboard-ready metric or sample table. |
| [`huggingface_hm_search_product_group_metrics.csv`](./processed/huggingface_hm_search_product_group_metrics.csv) | `processed` | 19 | 2 | Dashboard-ready metric or sample table. |
| [`huggingface_hm_search_product_type_metrics.csv`](./processed/huggingface_hm_search_product_type_metrics.csv) | `processed` | 131 | 2 | Dashboard-ready metric or sample table. |
| [`huggingface_hm_search_sales_channel_metrics.csv`](./processed/huggingface_hm_search_sales_channel_metrics.csv) | `processed` | 2 | 2 | Dashboard-ready metric or sample table. |
| [`huggingface_hm_search_top_article_transactions.csv`](./processed/huggingface_hm_search_top_article_transactions.csv) | `processed` | 1,000 | 2 | Dashboard-ready metric or sample table. |
| [`huggingface_hm_search_transaction_daily_metrics.csv`](./processed/huggingface_hm_search_transaction_daily_metrics.csv) | `processed` | 734 | 4 | Dashboard-ready metric or sample table. |
| [`huggingface_hm_search_transactions_sample.csv`](./processed/huggingface_hm_search_transactions_sample.csv) | `processed` | 1,000 | 5 | Dashboard-ready metric or sample table. |

## Column lists

### `huggingface_hm_search_articles_sample.csv`
`article_id`, `product_code`, `prod_name`, `product_type_no`, `product_type_name`, `product_group_name`, `graphical_appearance_no`, `graphical_appearance_name`, `colour_group_code`, `colour_group_name`, `perceived_colour_value_id`, `perceived_colour_value_name`, `perceived_colour_master_id`, `perceived_colour_master_name`, `department_no`, `department_name`, `index_code`, `index_name`, `index_group_no`, `index_group_name`, `section_no`, `section_name`, `garment_group_no`, `garment_group_name`, `detail_desc`

### `huggingface_hm_search_color_metrics.csv`
`colour_group_name`, `articles`

### `huggingface_hm_search_index_group_metrics.csv`
`index_group_name`, `articles`

### `huggingface_hm_search_product_group_metrics.csv`
`product_group_name`, `articles`

### `huggingface_hm_search_product_type_metrics.csv`
`product_type_name`, `articles`

### `huggingface_hm_search_sales_channel_metrics.csv`
`sales_channel_id`, `transactions`

### `huggingface_hm_search_top_article_transactions.csv`
`article_id`, `transactions`

### `huggingface_hm_search_transaction_daily_metrics.csv`
`date`, `transactions`, `price_sum`, `avg_price`

### `huggingface_hm_search_transactions_sample.csv`
`t_dat`, `customer_id`, `article_id`, `price`, `sales_channel_id`

Full field explanations are in [`../COLUMN_DICTIONARY.md`](../COLUMN_DICTIONARY.md).
