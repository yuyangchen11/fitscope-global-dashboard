# Kaggle H&M Personalized Fashion Recommendations

- Source: https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data
- Type: Real anonymized H&M apparel product and transaction data
- Purpose in FitScope: Provides apparel assortment structure, product hierarchy, article-level sample records and transaction momentum proxies.
- Boundary: No order status, returns, payment, margin, product cost, or traffic events.

## File inventory

| File | Layer | Rows | Columns | What it is used for |
|---|---|---:|---:|---|
| [`kaggle_hm_personalized_age_bucket_metrics.csv`](./processed/kaggle_hm_personalized_age_bucket_metrics.csv) | `processed` | 7 | 3 | Dashboard-ready metric or sample table. |
| [`kaggle_hm_personalized_articles_sample.csv`](./processed/kaggle_hm_personalized_articles_sample.csv) | `processed` | 1,000 | 9 | Dashboard-ready metric or sample table. |
| [`kaggle_hm_personalized_color_metrics.csv`](./processed/kaggle_hm_personalized_color_metrics.csv) | `processed` | 50 | 3 | Dashboard-ready metric or sample table. |
| [`kaggle_hm_personalized_customer_status_metrics.csv`](./processed/kaggle_hm_personalized_customer_status_metrics.csv) | `processed` | 4 | 3 | Dashboard-ready metric or sample table. |
| [`kaggle_hm_personalized_customers_sample.csv`](./processed/kaggle_hm_personalized_customers_sample.csv) | `processed` | 1,000 | 7 | Dashboard-ready metric or sample table. |
| [`kaggle_hm_personalized_fashion_news_metrics.csv`](./processed/kaggle_hm_personalized_fashion_news_metrics.csv) | `processed` | 5 | 3 | Dashboard-ready metric or sample table. |
| [`kaggle_hm_personalized_index_group_metrics.csv`](./processed/kaggle_hm_personalized_index_group_metrics.csv) | `processed` | 5 | 3 | Dashboard-ready metric or sample table. |
| [`kaggle_hm_personalized_product_group_metrics.csv`](./processed/kaggle_hm_personalized_product_group_metrics.csv) | `processed` | 19 | 3 | Dashboard-ready metric or sample table. |
| [`kaggle_hm_personalized_product_type_metrics.csv`](./processed/kaggle_hm_personalized_product_type_metrics.csv) | `processed` | 131 | 3 | Dashboard-ready metric or sample table. |
| [`kaggle_hm_personalized_sales_channel_metrics.csv`](./processed/kaggle_hm_personalized_sales_channel_metrics.csv) | `processed` | 2 | 3 | Dashboard-ready metric or sample table. |
| [`kaggle_hm_personalized_section_metrics.csv`](./processed/kaggle_hm_personalized_section_metrics.csv) | `processed` | 56 | 3 | Dashboard-ready metric or sample table. |
| [`kaggle_hm_personalized_summary.csv`](./processed/kaggle_hm_personalized_summary.csv) | `processed` | 5 | 2 | Dashboard-ready metric or sample table. |
| [`kaggle_hm_personalized_top_article_transactions.csv`](./processed/kaggle_hm_personalized_top_article_transactions.csv) | `processed` | 200 | 7 | Dashboard-ready metric or sample table. |
| [`kaggle_hm_personalized_transaction_articles_sample.csv`](./processed/kaggle_hm_personalized_transaction_articles_sample.csv) | `processed` | 815 | 9 | Dashboard-ready metric or sample table. |
| [`kaggle_hm_personalized_transaction_color_metrics.csv`](./processed/kaggle_hm_personalized_transaction_color_metrics.csv) | `processed` | 50 | 3 | Dashboard-ready metric or sample table. |
| [`kaggle_hm_personalized_transaction_daily_metrics.csv`](./processed/kaggle_hm_personalized_transaction_daily_metrics.csv) | `processed` | 734 | 4 | Dashboard-ready metric or sample table. |
| [`kaggle_hm_personalized_transaction_index_group_metrics.csv`](./processed/kaggle_hm_personalized_transaction_index_group_metrics.csv) | `processed` | 5 | 3 | Dashboard-ready metric or sample table. |
| [`kaggle_hm_personalized_transaction_product_group_metrics.csv`](./processed/kaggle_hm_personalized_transaction_product_group_metrics.csv) | `processed` | 19 | 3 | Dashboard-ready metric or sample table. |
| [`kaggle_hm_personalized_transaction_product_type_metrics.csv`](./processed/kaggle_hm_personalized_transaction_product_type_metrics.csv) | `processed` | 130 | 3 | Dashboard-ready metric or sample table. |
| [`kaggle_hm_personalized_transactions_sample.csv`](./processed/kaggle_hm_personalized_transactions_sample.csv) | `processed` | 1,000 | 5 | Dashboard-ready metric or sample table. |

## Column lists

### `kaggle_hm_personalized_age_bucket_metrics.csv`
`age_bucket`, `customers`, `share`

### `kaggle_hm_personalized_articles_sample.csv`
`article_id`, `prod_name`, `product_type_name`, `product_group_name`, `colour_group_name`, `index_group_name`, `section_name`, `garment_group_name`, `detail_desc`

### `kaggle_hm_personalized_color_metrics.csv`
`colour_group_name`, `articles`, `share`

### `kaggle_hm_personalized_customer_status_metrics.csv`
`club_member_status`, `customers`, `share`

### `kaggle_hm_personalized_customers_sample.csv`
`customer_id`, `FN`, `Active`, `club_member_status`, `fashion_news_frequency`, `age`, `postal_code`

### `kaggle_hm_personalized_fashion_news_metrics.csv`
`fashion_news_frequency`, `customers`, `share`

### `kaggle_hm_personalized_index_group_metrics.csv`
`index_group_name`, `articles`, `share`

### `kaggle_hm_personalized_product_group_metrics.csv`
`product_group_name`, `articles`, `share`

### `kaggle_hm_personalized_product_type_metrics.csv`
`product_type_name`, `articles`, `share`

### `kaggle_hm_personalized_sales_channel_metrics.csv`
`sales_channel_id`, `transactions`, `share`

### `kaggle_hm_personalized_section_metrics.csv`
`section_name`, `articles`, `share`

### `kaggle_hm_personalized_summary.csv`
`metric`, `value`

### `kaggle_hm_personalized_top_article_transactions.csv`
`article_id`, `transactions`, `prod_name`, `product_group_name`, `product_type_name`, `index_group_name`, `colour_group_name`

### `kaggle_hm_personalized_transaction_articles_sample.csv`
`article_id`, `prod_name`, `product_type_name`, `product_group_name`, `colour_group_name`, `index_group_name`, `section_name`, `garment_group_name`, `detail_desc`

### `kaggle_hm_personalized_transaction_color_metrics.csv`
`colour_group_name`, `transactions`, `share`

### `kaggle_hm_personalized_transaction_daily_metrics.csv`
`date`, `transactions`, `price_sum`, `avg_price`

### `kaggle_hm_personalized_transaction_index_group_metrics.csv`
`index_group_name`, `transactions`, `share`

### `kaggle_hm_personalized_transaction_product_group_metrics.csv`
`product_group_name`, `transactions`, `share`

### `kaggle_hm_personalized_transaction_product_type_metrics.csv`
`product_type_name`, `transactions`, `share`

### `kaggle_hm_personalized_transactions_sample.csv`
`t_dat`, `customer_id`, `article_id`, `price`, `sales_channel_id`

Full field explanations are in [`../COLUMN_DICTIONARY.md`](../COLUMN_DICTIONARY.md).
