# FitScope Commerce OS Data Architecture

## Current MVP

The website currently runs as a static frontend with CSV data adapters.

```
CSV files -> browser CSV parser -> normalized in-memory models -> dashboard views
```

This is acceptable for the independent study MVP because it keeps the demo portable and easy to share through GitHub Pages.

## Production Direction

The next version should keep the same frontend views but replace static CSV loading with an API layer.

```
PostgreSQL / Supabase
  -> scheduled ingestion jobs
  -> metric tables and semantic evidence tables
  -> REST API or edge functions
  -> dashboard frontend
```

## Core Tables

| Table | Purpose | Example Fields |
|---|---|---|
| `products` | Product and category master data | `product_id`, `sku`, `category`, `product_group`, `size`, `color`, `season`, `price` |
| `orders` | Sales and demand signals | `order_id`, `order_date`, `sku`, `quantity`, `revenue`, `discount`, `channel` |
| `returns` | Company KPI layer | `order_id`, `sku`, `is_returned`, `return_reason`, `refund_amount` |
| `reviews` | User evidence | `review_id`, `sku`, `category`, `rating`, `review_text`, `fit`, `body_type`, `occasion` |
| `semantic_tags` | Text analytics layer | `review_id`, `pain_point`, `sentiment`, `confidence` |
| `category_metrics` | Dashboard-ready aggregates | `category`, `demand_share`, `conversion_rate`, `return_rate`, `margin`, `risk_score` |

## Data Contract

Every dashboard view should read from normalized metric objects, not from raw files directly.

This lets the frontend keep the same interaction logic when the backend changes from CSV to PostgreSQL or Supabase.

## Dataset Upgrade Priority

1. Add a sales and returns dataset to replace modeled company KPIs.
2. Add SKU-level apparel sales with `size`, `color`, and `revenue` for assortment diagnostics.
3. Keep UCSD and review datasets for fit and semantic evidence.
4. Use Google Trends later as an external refreshable demand proxy, not as the only market signal.
