# FitScope Commerce OS: Real Dataset Evaluation

Updated: 2026-07-02

## Decision

No public real-world dataset found covers the complete apparel commerce chain of
traffic, product/SKU attributes, orders, returns with reasons, cost and margin,
reviews, and fit feedback.

Use a layered dataset architecture. Do not join unrelated sources at SKU or
customer level and do not present modeled fields as observed company KPIs.

## Recommended Stack

| Layer | Dataset | Reality / License | Dashboard use | Main limitation |
|---|---|---|---|---|
| Commerce operations | [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) | Real anonymized commercial data; CC BY-NC-SA 4.0 | Orders, order lines, status, payments, freight, delivery SLA, customers, sellers, product category and reviews | Not apparel-only; no true return reason, cost or gross margin |
| Apparel assortment | [H&M Personalized Fashion Recommendations](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data) | Real anonymized H&M data; competition terms | Apparel product hierarchy, article/SKU mix, customer purchases and transaction momentum | No order status, returns, payment, traffic or cost |
| China behavior funnel | [Tmall Repeat Buyers Prediction](https://tianchi.aliyun.com/competition/entrance/231576/information) | Real desensitized Tmall behavior; competition terms | Click, cart, favorite, purchase funnel; merchant, brand, item and repeat-purchase analysis | Categories are anonymized; no price, revenue, return or product text |
| Review semantics | [Amazon Reviews 2023](https://amazon-reviews-2023.github.io/) `Clothing_Shoes_and_Jewelry` | Real review and item metadata; research dataset terms | Ratings, review text, verified purchase, helpful votes, product metadata, price and images | Not linked to H&M/Olist; no order, return or margin facts |
| Fit evidence | Existing UCSD ModCloth / Rent the Runway data | Real historical review/fit data | Fit outcome, body type, size and occasion evidence | Historical and not linked to operational orders |

## Priority Ranking

### 1. Olist: best immediate addition

Olist is the closest match to the current Operations and order-detail pages. It
contains about 100,000 marketplace orders from 2016-2018 and separates facts and
dimensions into orders, order items, payments, products, customers, sellers,
reviews and geolocation tables.

Directly supported metrics:

- GMV: sum of order-item price for the chosen valid order statuses.
- Orders and units: distinct order IDs and order-item rows.
- Average order value: payment value or item revenue divided by orders.
- Cancellation rate: cancelled or unavailable orders divided by created orders.
- Delivery SLA: delivered date minus estimated or purchase date.
- Freight ratio: freight value divided by item value.
- Review score and review volume by product category.
- Seller, customer geography and payment-method mix.

Not supported and therefore not to be shown as observed:

- Return rate and return reasons.
- Product cost and gross margin.
- Page views, add-to-cart rate and conversion rate.
- Apparel fit, size and color attributes.

Recommended scope: filter Olist product categories to fashion-related categories
for the product-facing views, while retaining all categories only for marketplace
benchmarks. Keep Portuguese-to-English category translation as a dimension table.

### 2. Tmall repeat-buyer data: best China-market behavior layer

This official Tianchi competition provides user, item, category, merchant, brand,
date and action type. Action type distinguishes click, add-to-cart, purchase and
favorite. It also includes age range, gender and repeat-buyer labels.

Directly supported metrics:

- Click-to-cart, cart-to-purchase and click-to-purchase funnel ratios.
- Active users, buyers and repeat-buyer rate by merchant.
- Item, brand and merchant popularity.
- Cohort analysis by age range and gender.
- Double-11 period behavior and repeat-purchase modeling.

Limitations:

- Category IDs are desensitized, so it cannot honestly be labeled as apparel
  unless a valid category mapping is supplied.
- There is no price, GMV, order status, return or review text.
- The historical period is useful for methodology, not current-market reporting.

Use it on a separately labeled China behavior page or benchmark module. Do not
merge its user/item IDs with H&M or Olist.

### 3. Amazon Reviews 2023: best upgrade to semantic evidence

The Clothing, Shoes and Jewelry subset contains 66 million ratings across roughly
7.2 million items and 22.6 million users. Reviews include rating, text, timestamp,
helpful votes, verified purchase and item IDs. Metadata includes product title,
description, features, price and images.

Directly supported metrics:

- Review volume, average rating and low-rating share over time.
- Verified-purchase review share.
- Aspect-level pain points by product/category.
- Pain-point trend, helpfulness and representative evidence samples.
- Product metadata and image-backed SKU inspection.

Limitations:

- No actual order quantity, returns, traffic or margin.
- The complete subset is very large; use a reproducible filtered sample or a
  selected subcategory rather than downloading all raw files.

### 4. Retailrocket: optional funnel benchmark

[Retailrocket](https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset)
contains 2.76 million real events (view, add-to-cart and transaction), item
properties and a category tree. It is useful for event funnels and availability
analysis, but item properties are hashed and the category semantics are not
apparel-specific. It is a weaker fit than the Tmall dataset for this project.

### 5. UCI Online Retail II: clean fallback, weak topic fit

[Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii) has
1,067,371 real transaction rows with invoice, item code, description, quantity,
timestamp, unit price, customer and country. Invoice numbers beginning with `C`
identify cancellations. Its CC BY 4.0 license is clear, but the retailer sells
giftware rather than apparel and offers no product hierarchy, review or fit data.

## What Not To Promote As Real Company Data

The following local or previously shortlisted sources may remain useful for UI
testing, but must be labeled modeled or synthetic:

- Retail Fashion Boutique Data Sales Analytics 2025.
- Generic ecommerce order/return datasets that explicitly say simulated or
  synthetic.
- Locally generated company KPI, channel, store, margin or return-reason fields.

Rich schemas are not evidence of real commercial provenance.

## Dashboard Consequences

| Current metric or module | Real source | Decision |
|---|---|---|
| Apparel assortment and transaction share | H&M | Keep |
| Order detail, status, payment, freight, delivery | Olist | Replace local modeled order layer |
| Revenue / GMV | Olist or H&M transaction price | Show only when the source contains observed price |
| Conversion rate | Tmall or Retailrocket behavior events | Move to behavior context; do not calculate from orders alone |
| Return rate / return reason | No suitable real source found | Remove as observed KPI or label as modeled scenario |
| Gross margin | No suitable real source found | Remove until cost data exists |
| Review and pain-point semantics | Amazon Reviews 2023 + UCSD | Upgrade evidence layer |
| Fit and body-type risk | UCSD | Keep as an external evidence benchmark |
| China-market behavior | Tmall | Add as a separate benchmark, not a joined company fact |

## Implementation Status

Completed on 2026-07-02:

1. Downloaded all nine Olist source tables and retained the raw CSV files.
2. Added a reproducible processor that generates dashboard-ready summary,
   category, product, daily, status, payment and fashion order-line tables.
3. Replaced modeled order detail, revenue, delivery and review KPIs with Olist
   facts in Overview and Operations.
4. Kept H&M as the separately labeled apparel market and assortment layer.
5. Kept UCSD as the separately labeled fit and review-evidence benchmark.
6. Removed observed claims for return rate, return reason, gross margin and
   conversion where no source field exists.

Next candidates are a filtered Amazon fashion-review sample and, only if a China
behavior benchmark is in scope, the Tmall repeat-buyer data. Neither may be
row-level joined to Olist, H&M or UCSD.

## Acceptance Rule

A KPI is labeled `Observed` only when its numerator and denominator come from the
same real dataset and share a documented join key. Cross-source comparisons may
be shown as benchmarks, but cross-source row-level joins are prohibited.
