# Dataset Candidates for FitScope Commerce OS

## Recommendation

Prioritize datasets that can replace the current modeled company KPI layer. The dashboard needs sales, returns, margin, SKU, size, color, and category fields more than another generic review dataset.

## Candidate Ranking

| Priority | Dataset | Link | Why It Fits | Caveat |
|---|---|---|---|---|
| 1 | Retail Fashion Boutique Data Sales Analytics 2025 | https://www.kaggle.com/datasets/pratyushpuri/retail-fashion-boutique-data-sales-analytics-2025 | Apparel retail scope with return analytics. Apache 2.0 license is clearer for project use. Can support return-rate and category-readiness KPIs. | Synthetic dataset, so it should be labeled as a modeled company proxy. |
| 2 | Women Clothing Ecommerce Sales Data | https://www.kaggle.com/datasets/shilongzhuang/-women-clothing-ecommerce-sales-data | Real-life women’s clothing ecommerce sales data from a shop. Strong fit for SKU, size, color, revenue, and assortment questions. | License is listed as “Other”, so usage needs page-level confirmation before publishing processed extracts. |
| 3 | Ecommerce Sales Data 2023-2024 - for Pandas | https://www.kaggle.com/datasets/kunalwaghai/ecommerce-sales-data-2023-2024 | MIT license and transaction-level ecommerce structure. Useful as a generic sales baseline if apparel-specific datasets are insufficient. | Not apparel-specific, weaker topic fit. |
| 4 | Women’s E-Commerce Clothing Reviews | https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews | Already aligned with review text, rating, department, and class-level semantic analysis. | Review evidence only, not company sales or returns. |

## GitHub Findings

GitHub search returned mostly analysis projects built on Women’s E-Commerce Clothing Reviews, not stronger raw data sources.

Examples:

| Repository | Link | Usefulness |
|---|---|---|
| women-clothing-ecommerce-data-analysis | https://github.com/Foram2248/women-clothing-ecommerce-data-analysis | Useful for analysis inspiration, not a primary data source. |
| Womens_Ecommerce_Clothing_Analysis | https://github.com/ntthuylinh144/Womens_Ecommerce_Clothing_Analysis | Points back to the Kaggle women’s reviews dataset. |
| Ecommerce_women_clothing | https://github.com/ZeeTsing/Ecommerce_women_clothing | NLP and sentiment-analysis reference. |
| EcommerceReviews | https://github.com/busekcoban/EcommerceReviews | SQL analysis reference for the reviews dataset. |

## Integration Plan

1. Download the Apache 2.0 retail fashion boutique dataset first.
2. Inspect columns and map them to `orders`, `returns`, `products`, and `category_metrics`.
3. If the women clothing sales dataset license is acceptable, add it as a SKU-level apparel sales source.
4. Replace current modeled company KPI calculations with processed aggregates:
   - `conversion_proxy`
   - `return_rate`
   - `refund_rate`
   - `gross_margin_proxy`
   - `category_revenue`
   - `size_color_mix`
5. Keep review and fit datasets as evidence layers rather than company KPI layers.
