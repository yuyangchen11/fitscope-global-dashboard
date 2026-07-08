# Data Catalog

This folder stores all CSV data used or staged for FitScope Commerce OS. The project intentionally keeps dashboard-ready CSV files unzipped so GitHub can preview them and the static dashboard can fetch them directly. Large production datasets should move to database storage or Git LFS if a single file exceeds GitHub limits.

## Folder rule

| Folder layer | Meaning | Commit rule |
|---|---|---|
| `raw/` | Source-shaped files downloaded or staged with minimal edits | Commit only public/anonymized CSV under GitHub size limits |
| `processed/` | Dashboard-ready aggregates, samples, and normalized tables | Commit directly as CSV |

## Data sources

| Folder | Source | Role in product | Raw files | Processed files |
|---|---|---|---:|---:|
| `huggingface_hm_search/` | Hugging Face H&M Search / Sample Mirror | Provides lightweight H&M-like processed metrics for fallback testing and dashboard development. | 0 | 9 |
| `kaggle_fashion_boutique/` | Kaggle Retail Fashion Boutique Data Sales Analytics 2025 | Provides category KPI proxy fields such as price, rating, return flag, return reason, markdown and stock for operating readiness. | 1 | 3 |
| `kaggle_hm_personalized/` | Kaggle H&M Personalized Fashion Recommendations | Provides apparel assortment structure, product hierarchy, article-level sample records and transaction momentum proxies. | 0 | 20 |
| `kaggle_olist/` | Kaggle Olist Brazilian E-Commerce | Provides the closest real commerce operations layer: orders, order lines, payment, delivery, freight, review score, seller/customer geography and fashion product-level detail. | 9 | 7 |
| `kaggle_womens_reviews/` | Kaggle Women Clothing Reviews | Provides review class and sentiment benchmark metrics for the evidence and semantic views. | 0 | 2 |
| `kaggle_womens_sales/` | Kaggle Women Clothing Ecommerce Sales | Provides SKU/order/date/size/color/price/quantity/revenue structure for order-detail and SKU drill-down design validation. | 1 | 3 |
| `ucsd_clothing_fit/` | UCSD Clothing Fit Feedback | Provides fit outcome, body type, size and review evidence used for fit-risk and review pain-point diagnosis. | 0 | 5 |

## Files

| CSV | Source | Layer | Rows | Columns | Size |
|---|---|---|---:|---:|---:|
| [`data/huggingface_hm_search/processed/huggingface_hm_search_articles_sample.csv`](./huggingface_hm_search/processed/huggingface_hm_search_articles_sample.csv) | `huggingface_hm_search` | `processed` | 1,000 | 25 | 0.3 MB |
| [`data/huggingface_hm_search/processed/huggingface_hm_search_color_metrics.csv`](./huggingface_hm_search/processed/huggingface_hm_search_color_metrics.csv) | `huggingface_hm_search` | `processed` | 50 | 2 | 0.0 MB |
| [`data/huggingface_hm_search/processed/huggingface_hm_search_index_group_metrics.csv`](./huggingface_hm_search/processed/huggingface_hm_search_index_group_metrics.csv) | `huggingface_hm_search` | `processed` | 5 | 2 | 0.0 MB |
| [`data/huggingface_hm_search/processed/huggingface_hm_search_product_group_metrics.csv`](./huggingface_hm_search/processed/huggingface_hm_search_product_group_metrics.csv) | `huggingface_hm_search` | `processed` | 19 | 2 | 0.0 MB |
| [`data/huggingface_hm_search/processed/huggingface_hm_search_product_type_metrics.csv`](./huggingface_hm_search/processed/huggingface_hm_search_product_type_metrics.csv) | `huggingface_hm_search` | `processed` | 131 | 2 | 0.0 MB |
| [`data/huggingface_hm_search/processed/huggingface_hm_search_sales_channel_metrics.csv`](./huggingface_hm_search/processed/huggingface_hm_search_sales_channel_metrics.csv) | `huggingface_hm_search` | `processed` | 2 | 2 | 0.0 MB |
| [`data/huggingface_hm_search/processed/huggingface_hm_search_top_article_transactions.csv`](./huggingface_hm_search/processed/huggingface_hm_search_top_article_transactions.csv) | `huggingface_hm_search` | `processed` | 1,000 | 2 | 0.0 MB |
| [`data/huggingface_hm_search/processed/huggingface_hm_search_transaction_daily_metrics.csv`](./huggingface_hm_search/processed/huggingface_hm_search_transaction_daily_metrics.csv) | `huggingface_hm_search` | `processed` | 734 | 4 | 0.0 MB |
| [`data/huggingface_hm_search/processed/huggingface_hm_search_transactions_sample.csv`](./huggingface_hm_search/processed/huggingface_hm_search_transactions_sample.csv) | `huggingface_hm_search` | `processed` | 1,000 | 5 | 0.1 MB |
| [`data/kaggle_fashion_boutique/processed/kaggle_fashion_boutique_company_category_kpi.csv`](./kaggle_fashion_boutique/processed/kaggle_fashion_boutique_company_category_kpi.csv) | `kaggle_fashion_boutique` | `processed` | 6 | 14 | 0.0 MB |
| [`data/kaggle_fashion_boutique/processed/kaggle_fashion_boutique_daily_kpi.csv`](./kaggle_fashion_boutique/processed/kaggle_fashion_boutique_daily_kpi.csv) | `kaggle_fashion_boutique` | `processed` | 273 | 5 | 0.0 MB |
| [`data/kaggle_fashion_boutique/processed/kaggle_fashion_boutique_return_reason_metrics.csv`](./kaggle_fashion_boutique/processed/kaggle_fashion_boutique_return_reason_metrics.csv) | `kaggle_fashion_boutique` | `processed` | 36 | 4 | 0.0 MB |
| [`data/kaggle_fashion_boutique/raw/kaggle_fashion_boutique_dataset.csv`](./kaggle_fashion_boutique/raw/kaggle_fashion_boutique_dataset.csv) | `kaggle_fashion_boutique` | `raw` | 2,176 | 14 | 0.2 MB |
| [`data/kaggle_hm_personalized/processed/kaggle_hm_personalized_age_bucket_metrics.csv`](./kaggle_hm_personalized/processed/kaggle_hm_personalized_age_bucket_metrics.csv) | `kaggle_hm_personalized` | `processed` | 7 | 3 | 0.0 MB |
| [`data/kaggle_hm_personalized/processed/kaggle_hm_personalized_articles_sample.csv`](./kaggle_hm_personalized/processed/kaggle_hm_personalized_articles_sample.csv) | `kaggle_hm_personalized` | `processed` | 1,000 | 9 | 0.2 MB |
| [`data/kaggle_hm_personalized/processed/kaggle_hm_personalized_color_metrics.csv`](./kaggle_hm_personalized/processed/kaggle_hm_personalized_color_metrics.csv) | `kaggle_hm_personalized` | `processed` | 50 | 3 | 0.0 MB |
| [`data/kaggle_hm_personalized/processed/kaggle_hm_personalized_customer_status_metrics.csv`](./kaggle_hm_personalized/processed/kaggle_hm_personalized_customer_status_metrics.csv) | `kaggle_hm_personalized` | `processed` | 4 | 3 | 0.0 MB |
| [`data/kaggle_hm_personalized/processed/kaggle_hm_personalized_customers_sample.csv`](./kaggle_hm_personalized/processed/kaggle_hm_personalized_customers_sample.csv) | `kaggle_hm_personalized` | `processed` | 1,000 | 7 | 0.1 MB |
| [`data/kaggle_hm_personalized/processed/kaggle_hm_personalized_fashion_news_metrics.csv`](./kaggle_hm_personalized/processed/kaggle_hm_personalized_fashion_news_metrics.csv) | `kaggle_hm_personalized` | `processed` | 5 | 3 | 0.0 MB |
| [`data/kaggle_hm_personalized/processed/kaggle_hm_personalized_index_group_metrics.csv`](./kaggle_hm_personalized/processed/kaggle_hm_personalized_index_group_metrics.csv) | `kaggle_hm_personalized` | `processed` | 5 | 3 | 0.0 MB |
| [`data/kaggle_hm_personalized/processed/kaggle_hm_personalized_product_group_metrics.csv`](./kaggle_hm_personalized/processed/kaggle_hm_personalized_product_group_metrics.csv) | `kaggle_hm_personalized` | `processed` | 19 | 3 | 0.0 MB |
| [`data/kaggle_hm_personalized/processed/kaggle_hm_personalized_product_type_metrics.csv`](./kaggle_hm_personalized/processed/kaggle_hm_personalized_product_type_metrics.csv) | `kaggle_hm_personalized` | `processed` | 131 | 3 | 0.0 MB |
| [`data/kaggle_hm_personalized/processed/kaggle_hm_personalized_sales_channel_metrics.csv`](./kaggle_hm_personalized/processed/kaggle_hm_personalized_sales_channel_metrics.csv) | `kaggle_hm_personalized` | `processed` | 2 | 3 | 0.0 MB |
| [`data/kaggle_hm_personalized/processed/kaggle_hm_personalized_section_metrics.csv`](./kaggle_hm_personalized/processed/kaggle_hm_personalized_section_metrics.csv) | `kaggle_hm_personalized` | `processed` | 56 | 3 | 0.0 MB |
| [`data/kaggle_hm_personalized/processed/kaggle_hm_personalized_summary.csv`](./kaggle_hm_personalized/processed/kaggle_hm_personalized_summary.csv) | `kaggle_hm_personalized` | `processed` | 5 | 2 | 0.0 MB |
| [`data/kaggle_hm_personalized/processed/kaggle_hm_personalized_top_article_transactions.csv`](./kaggle_hm_personalized/processed/kaggle_hm_personalized_top_article_transactions.csv) | `kaggle_hm_personalized` | `processed` | 200 | 7 | 0.0 MB |
| [`data/kaggle_hm_personalized/processed/kaggle_hm_personalized_transaction_articles_sample.csv`](./kaggle_hm_personalized/processed/kaggle_hm_personalized_transaction_articles_sample.csv) | `kaggle_hm_personalized` | `processed` | 815 | 9 | 0.2 MB |
| [`data/kaggle_hm_personalized/processed/kaggle_hm_personalized_transaction_color_metrics.csv`](./kaggle_hm_personalized/processed/kaggle_hm_personalized_transaction_color_metrics.csv) | `kaggle_hm_personalized` | `processed` | 50 | 3 | 0.0 MB |
| [`data/kaggle_hm_personalized/processed/kaggle_hm_personalized_transaction_daily_metrics.csv`](./kaggle_hm_personalized/processed/kaggle_hm_personalized_transaction_daily_metrics.csv) | `kaggle_hm_personalized` | `processed` | 734 | 4 | 0.0 MB |
| [`data/kaggle_hm_personalized/processed/kaggle_hm_personalized_transaction_index_group_metrics.csv`](./kaggle_hm_personalized/processed/kaggle_hm_personalized_transaction_index_group_metrics.csv) | `kaggle_hm_personalized` | `processed` | 5 | 3 | 0.0 MB |
| [`data/kaggle_hm_personalized/processed/kaggle_hm_personalized_transaction_product_group_metrics.csv`](./kaggle_hm_personalized/processed/kaggle_hm_personalized_transaction_product_group_metrics.csv) | `kaggle_hm_personalized` | `processed` | 19 | 3 | 0.0 MB |
| [`data/kaggle_hm_personalized/processed/kaggle_hm_personalized_transaction_product_type_metrics.csv`](./kaggle_hm_personalized/processed/kaggle_hm_personalized_transaction_product_type_metrics.csv) | `kaggle_hm_personalized` | `processed` | 130 | 3 | 0.0 MB |
| [`data/kaggle_hm_personalized/processed/kaggle_hm_personalized_transactions_sample.csv`](./kaggle_hm_personalized/processed/kaggle_hm_personalized_transactions_sample.csv) | `kaggle_hm_personalized` | `processed` | 1,000 | 5 | 0.1 MB |
| [`data/kaggle_olist/processed/olist_category_metrics.csv`](./kaggle_olist/processed/olist_category_metrics.csv) | `kaggle_olist` | `processed` | 74 | 17 | 0.0 MB |
| [`data/kaggle_olist/processed/olist_daily_metrics.csv`](./kaggle_olist/processed/olist_daily_metrics.csv) | `kaggle_olist` | `processed` | 616 | 7 | 0.0 MB |
| [`data/kaggle_olist/processed/olist_fashion_order_lines.csv`](./kaggle_olist/processed/olist_fashion_order_lines.csv) | `kaggle_olist` | `processed` | 2,642 | 17 | 0.6 MB |
| [`data/kaggle_olist/processed/olist_order_status_metrics.csv`](./kaggle_olist/processed/olist_order_status_metrics.csv) | `kaggle_olist` | `processed` | 8 | 3 | 0.0 MB |
| [`data/kaggle_olist/processed/olist_payment_metrics.csv`](./kaggle_olist/processed/olist_payment_metrics.csv) | `kaggle_olist` | `processed` | 5 | 3 | 0.0 MB |
| [`data/kaggle_olist/processed/olist_product_metrics.csv`](./kaggle_olist/processed/olist_product_metrics.csv) | `kaggle_olist` | `processed` | 1,221 | 12 | 0.1 MB |
| [`data/kaggle_olist/processed/olist_summary.csv`](./kaggle_olist/processed/olist_summary.csv) | `kaggle_olist` | `processed` | 1 | 14 | 0.0 MB |
| [`data/kaggle_olist/raw/olist_customers_dataset.csv`](./kaggle_olist/raw/olist_customers_dataset.csv) | `kaggle_olist` | `raw` | 99,441 | 5 | 8.6 MB |
| [`data/kaggle_olist/raw/olist_geolocation_dataset.csv`](./kaggle_olist/raw/olist_geolocation_dataset.csv) | `kaggle_olist` | `raw` | 1,000,163 | 5 | 58.4 MB |
| [`data/kaggle_olist/raw/olist_order_items_dataset.csv`](./kaggle_olist/raw/olist_order_items_dataset.csv) | `kaggle_olist` | `raw` | 112,650 | 7 | 14.7 MB |
| [`data/kaggle_olist/raw/olist_order_payments_dataset.csv`](./kaggle_olist/raw/olist_order_payments_dataset.csv) | `kaggle_olist` | `raw` | 103,886 | 5 | 5.5 MB |
| [`data/kaggle_olist/raw/olist_order_reviews_dataset.csv`](./kaggle_olist/raw/olist_order_reviews_dataset.csv) | `kaggle_olist` | `raw` | 104,719 | 7 | 13.8 MB |
| [`data/kaggle_olist/raw/olist_orders_dataset.csv`](./kaggle_olist/raw/olist_orders_dataset.csv) | `kaggle_olist` | `raw` | 99,441 | 8 | 16.8 MB |
| [`data/kaggle_olist/raw/olist_products_dataset.csv`](./kaggle_olist/raw/olist_products_dataset.csv) | `kaggle_olist` | `raw` | 32,951 | 9 | 2.3 MB |
| [`data/kaggle_olist/raw/olist_sellers_dataset.csv`](./kaggle_olist/raw/olist_sellers_dataset.csv) | `kaggle_olist` | `raw` | 3,095 | 4 | 0.2 MB |
| [`data/kaggle_olist/raw/product_category_name_translation.csv`](./kaggle_olist/raw/product_category_name_translation.csv) | `kaggle_olist` | `raw` | 71 | 2 | 0.0 MB |
| [`data/kaggle_womens_reviews/processed/kaggle_womens_reviews_class_metrics.csv`](./kaggle_womens_reviews/processed/kaggle_womens_reviews_class_metrics.csv) | `kaggle_womens_reviews` | `processed` | 21 | 5 | 0.0 MB |
| [`data/kaggle_womens_reviews/processed/kaggle_womens_reviews_sentiment_metrics.csv`](./kaggle_womens_reviews/processed/kaggle_womens_reviews_sentiment_metrics.csv) | `kaggle_womens_reviews` | `processed` | 3 | 2 | 0.0 MB |
| [`data/kaggle_womens_sales/processed/kaggle_womens_sales_daily_metrics.csv`](./kaggle_womens_sales/processed/kaggle_womens_sales_daily_metrics.csv) | `kaggle_womens_sales` | `processed` | 116 | 6 | 0.0 MB |
| [`data/kaggle_womens_sales/processed/kaggle_womens_sales_size_metrics.csv`](./kaggle_womens_sales/processed/kaggle_womens_sales_size_metrics.csv) | `kaggle_womens_sales` | `processed` | 10 | 5 | 0.0 MB |
| [`data/kaggle_womens_sales/processed/kaggle_womens_sales_sku_metrics.csv`](./kaggle_womens_sales/processed/kaggle_womens_sales_sku_metrics.csv) | `kaggle_womens_sales` | `processed` | 24 | 8 | 0.0 MB |
| [`data/kaggle_womens_sales/raw/kaggle_womens_sales_orders.csv`](./kaggle_womens_sales/raw/kaggle_womens_sales_orders.csv) | `kaggle_womens_sales` | `raw` | 527 | 8 | 0.0 MB |
| [`data/ucsd_clothing_fit/processed/ucsd_body_type_metrics.csv`](./ucsd_clothing_fit/processed/ucsd_body_type_metrics.csv) | `ucsd_clothing_fit` | `processed` | 8 | 12 | 0.0 MB |
| [`data/ucsd_clothing_fit/processed/ucsd_category_metrics.csv`](./ucsd_clothing_fit/processed/ucsd_category_metrics.csv) | `ucsd_clothing_fit` | `processed` | 60 | 12 | 0.0 MB |
| [`data/ucsd_clothing_fit/processed/ucsd_evidence_sample.csv`](./ucsd_clothing_fit/processed/ucsd_evidence_sample.csv) | `ucsd_clothing_fit` | `processed` | 1,000 | 25 | 0.5 MB |
| [`data/ucsd_clothing_fit/processed/ucsd_pain_point_metrics.csv`](./ucsd_clothing_fit/processed/ucsd_pain_point_metrics.csv) | `ucsd_clothing_fit` | `processed` | 7 | 2 | 0.0 MB |
| [`data/ucsd_clothing_fit/processed/ucsd_size_metrics.csv`](./ucsd_clothing_fit/processed/ucsd_size_metrics.csv) | `ucsd_clothing_fit` | `processed` | 57 | 12 | 0.0 MB |

See [`COLUMN_DICTIONARY.md`](./COLUMN_DICTIONARY.md) for field-level explanations and first-row samples.
