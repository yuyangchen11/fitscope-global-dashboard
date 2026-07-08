# Kaggle Olist Brazilian E-Commerce

- Source: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
- Type: Real anonymized marketplace order data
- Purpose in FitScope: Provides the closest real commerce operations layer: orders, order lines, payment, delivery, freight, review score, seller/customer geography and fashion product-level detail.
- Boundary: No true return reason, product cost, gross margin, traffic, impression, or conversion funnel fields.

## File inventory

| File | Layer | Rows | Columns | What it is used for |
|---|---|---:|---:|---|
| [`olist_category_metrics.csv`](./processed/olist_category_metrics.csv) | `processed` | 74 | 17 | Dashboard-ready metric or sample table. |
| [`olist_daily_metrics.csv`](./processed/olist_daily_metrics.csv) | `processed` | 616 | 7 | Dashboard-ready metric or sample table. |
| [`olist_fashion_order_lines.csv`](./processed/olist_fashion_order_lines.csv) | `processed` | 2,642 | 17 | Dashboard-ready metric or sample table. |
| [`olist_order_status_metrics.csv`](./processed/olist_order_status_metrics.csv) | `processed` | 8 | 3 | Dashboard-ready metric or sample table. |
| [`olist_payment_metrics.csv`](./processed/olist_payment_metrics.csv) | `processed` | 5 | 3 | Dashboard-ready metric or sample table. |
| [`olist_product_metrics.csv`](./processed/olist_product_metrics.csv) | `processed` | 1,221 | 12 | Dashboard-ready metric or sample table. |
| [`olist_summary.csv`](./processed/olist_summary.csv) | `processed` | 1 | 14 | Dashboard-ready metric or sample table. |
| [`olist_customers_dataset.csv`](./raw/olist_customers_dataset.csv) | `raw` | 99,441 | 5 | Original source-shaped CSV. |
| [`olist_geolocation_dataset.csv`](./raw/olist_geolocation_dataset.csv) | `raw` | 1,000,163 | 5 | Original source-shaped CSV. |
| [`olist_order_items_dataset.csv`](./raw/olist_order_items_dataset.csv) | `raw` | 112,650 | 7 | Original source-shaped CSV. |
| [`olist_order_payments_dataset.csv`](./raw/olist_order_payments_dataset.csv) | `raw` | 103,886 | 5 | Original source-shaped CSV. |
| [`olist_order_reviews_dataset.csv`](./raw/olist_order_reviews_dataset.csv) | `raw` | 104,719 | 7 | Original source-shaped CSV. |
| [`olist_orders_dataset.csv`](./raw/olist_orders_dataset.csv) | `raw` | 99,441 | 8 | Original source-shaped CSV. |
| [`olist_products_dataset.csv`](./raw/olist_products_dataset.csv) | `raw` | 32,951 | 9 | Original source-shaped CSV. |
| [`olist_sellers_dataset.csv`](./raw/olist_sellers_dataset.csv) | `raw` | 3,095 | 4 | Original source-shaped CSV. |
| [`product_category_name_translation.csv`](./raw/product_category_name_translation.csv) | `raw` | 71 | 2 | Original source-shaped CSV. |

## Column lists

### `olist_category_metrics.csv`
`category`, `scope`, `orders`, `units`, `products`, `sellers`, `customers`, `revenue`, `avg_item_price`, `freight_value`, `freight_ratio`, `avg_review_score`, `review_count`, `on_time_rate`, `late_delivery_rate`, `cancelled_line_rate`, `latest_order`

### `olist_daily_metrics.csv`
`date`, `orders`, `units`, `revenue`, `freight_value`, `avg_review_score`, `on_time_rate`

### `olist_fashion_order_lines.csv`
`line_id`, `order_id`, `order_time`, `order_status`, `product_id`, `category`, `seller_id`, `customer_state`, `unit_price`, `freight_value`, `line_total`, `payment_type`, `installments`, `review_score`, `delivered_at`, `estimated_delivery`, `delivery_status`

### `olist_order_status_metrics.csv`
`order_status`, `orders`, `share`

### `olist_payment_metrics.csv`
`payment_type`, `records`, `payment_value`

### `olist_product_metrics.csv`
`product_id`, `category`, `orders`, `units`, `sellers`, `revenue`, `avg_item_price`, `freight_ratio`, `avg_review_score`, `review_count`, `on_time_rate`, `latest_order`

### `olist_summary.csv`
`orders`, `valid_orders`, `delivered_orders`, `cancelled_orders`, `cancellation_rate`, `revenue`, `average_order_value`, `on_time_delivery_rate`, `average_review_score`, `review_count`, `fashion_order_lines`, `fashion_products`, `start_date`, `end_date`

### `olist_customers_dataset.csv`
`customer_id`, `customer_unique_id`, `customer_zip_code_prefix`, `customer_city`, `customer_state`

### `olist_geolocation_dataset.csv`
`geolocation_zip_code_prefix`, `geolocation_lat`, `geolocation_lng`, `geolocation_city`, `geolocation_state`

### `olist_order_items_dataset.csv`
`order_id`, `order_item_id`, `product_id`, `seller_id`, `shipping_limit_date`, `price`, `freight_value`

### `olist_order_payments_dataset.csv`
`order_id`, `payment_sequential`, `payment_type`, `payment_installments`, `payment_value`

### `olist_order_reviews_dataset.csv`
`review_id`, `order_id`, `review_score`, `review_comment_title`, `review_comment_message`, `review_creation_date`, `review_answer_timestamp`

### `olist_orders_dataset.csv`
`order_id`, `customer_id`, `order_status`, `order_purchase_timestamp`, `order_approved_at`, `order_delivered_carrier_date`, `order_delivered_customer_date`, `order_estimated_delivery_date`

### `olist_products_dataset.csv`
`product_id`, `product_category_name`, `product_name_lenght`, `product_description_lenght`, `product_photos_qty`, `product_weight_g`, `product_length_cm`, `product_height_cm`, `product_width_cm`

### `olist_sellers_dataset.csv`
`seller_id`, `seller_zip_code_prefix`, `seller_city`, `seller_state`

### `product_category_name_translation.csv`
`product_category_name`, `product_category_name_english`

Full field explanations are in [`../COLUMN_DICTIONARY.md`](../COLUMN_DICTIONARY.md).
