# UCSD Clothing Fit Feedback

- Source: https://cseweb.ucsd.edu/~jmcauley/datasets.html#clothing_fit
- Type: Public fit feedback and review evidence
- Purpose in FitScope: Provides fit outcome, body type, size and review evidence used for fit-risk and review pain-point diagnosis.
- Boundary: Review/rental context is not a live store transaction table.

## File inventory

| File | Layer | Rows | Columns | What it is used for |
|---|---|---:|---:|---|
| [`ucsd_body_type_metrics.csv`](./processed/ucsd_body_type_metrics.csv) | `processed` | 8 | 12 | Dashboard-ready metric or sample table. |
| [`ucsd_category_metrics.csv`](./processed/ucsd_category_metrics.csv) | `processed` | 60 | 12 | Dashboard-ready metric or sample table. |
| [`ucsd_evidence_sample.csv`](./processed/ucsd_evidence_sample.csv) | `processed` | 1,000 | 25 | Dashboard-ready metric or sample table. |
| [`ucsd_pain_point_metrics.csv`](./processed/ucsd_pain_point_metrics.csv) | `processed` | 7 | 2 | Dashboard-ready metric or sample table. |
| [`ucsd_size_metrics.csv`](./processed/ucsd_size_metrics.csv) | `processed` | 57 | 12 | Dashboard-ready metric or sample table. |

## Column lists

### `ucsd_body_type_metrics.csv`
`body_type`, `records`, `display_eligible`, `fit_rate`, `too_small_rate`, `too_large_rate`, `nonfit_rate`, `low_signal_rate`, `pain_point_rate`, `avg_rating`, `avg_quality`, `risk_score`

### `ucsd_category_metrics.csv`
`category_group`, `records`, `display_eligible`, `fit_rate`, `too_small_rate`, `too_large_rate`, `nonfit_rate`, `low_signal_rate`, `pain_point_rate`, `avg_rating`, `avg_quality`, `risk_score`

### `ucsd_evidence_sample.csv`
`dataset`, `item_id`, `user_id`, `category_raw`, `category_group`, `fit`, `is_fit`, `is_small`, `is_large`, `is_nonfit`, `rating`, `quality`, `low_signal`, `size`, `height_inches`, `height_bucket`, `weight_lbs`, `weight_bucket`, `body_type`, `occasion`, `length`, `review_summary`, `review_text`, `pain_points`, `has_pain_point`

### `ucsd_pain_point_metrics.csv`
`pain_point`, `records`

### `ucsd_size_metrics.csv`
`size`, `records`, `display_eligible`, `fit_rate`, `too_small_rate`, `too_large_rate`, `nonfit_rate`, `low_signal_rate`, `pain_point_rate`, `avg_rating`, `avg_quality`, `risk_score`

Full field explanations are in [`../COLUMN_DICTIONARY.md`](../COLUMN_DICTIONARY.md).
