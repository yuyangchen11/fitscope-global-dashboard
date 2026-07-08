# Kaggle Women Clothing Reviews

- Source: https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews
- Type: Public women apparel review benchmark
- Purpose in FitScope: Provides review class and sentiment benchmark metrics for the evidence and semantic views.
- Boundary: No order-line economics or fulfillment data.

## File inventory

| File | Layer | Rows | Columns | What it is used for |
|---|---|---:|---:|---|
| [`kaggle_womens_reviews_class_metrics.csv`](./processed/kaggle_womens_reviews_class_metrics.csv) | `processed` | 21 | 5 | Dashboard-ready metric or sample table. |
| [`kaggle_womens_reviews_sentiment_metrics.csv`](./processed/kaggle_womens_reviews_sentiment_metrics.csv) | `processed` | 3 | 2 | Dashboard-ready metric or sample table. |

## Column lists

### `kaggle_womens_reviews_class_metrics.csv`
`class_name`, `records`, `avg_rating`, `recommended_rate`, `low_rating_rate`

### `kaggle_womens_reviews_sentiment_metrics.csv`
`sentiment_bucket`, `records`

Full field explanations are in [`../COLUMN_DICTIONARY.md`](../COLUMN_DICTIONARY.md).
