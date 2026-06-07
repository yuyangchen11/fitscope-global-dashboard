# Kaggle Fashion Boutique

Source: https://www.kaggle.com/datasets/pratyushpuri/retail-fashion-boutique-data-sales-analytics-2025

Purpose in dashboard:
- Provides the operating KPI layer for category readiness.
- Fields used: `category`, `current_price`, `customer_rating`, `is_returned`, `return_reason`, `stock_quantity`, `markdown_percentage`.
- Processed output `processed/kaggle_fashion_boutique_company_category_kpi.csv` is loaded by the Commerce OS frontend before fallback model values.

Current limitation:
- The dataset is positioned as an analytics dataset and should be treated as a company-KPI proxy until replaced by internal order, return, and margin data.
