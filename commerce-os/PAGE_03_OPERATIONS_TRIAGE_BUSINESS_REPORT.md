# Page 03 Business Report: Operations Health Dashboard

## 1. Executive Decision

The third dashboard should become an **Operations Health Dashboard**.

It should not be a relationship graph. It should not be a visual network. It should not read like a written report.

It should be a normal business dashboard where an operator can read the business condition from metrics, trends, tables, color states, and drill-downs.

Recommended page name:

| Language | Page Name |
|---|---|
| Chinese | 经营看板 |
| English | Operations Health |

This page should be table-led and KPI-led, because real operators need stable comparison, sorting, filters, and drill-down. The page should avoid long explanatory copy. Labels should be reusable across data refreshes.

## 1.1 Dashboard Principle

Use fewer sentences and more structured signals.

| Avoid | Use Instead |
|---|---|
| Current priority | Health score, risk score, status color |
| Long reason paragraph | Top 3 driver chips |
| Next step text block | icon buttons or compact action column |
| Business explanation card | sortable table, KPI card, trend, distribution |
| Fixed recommendation sentence | metric threshold and status badge |

The dashboard should feel like a live operating surface, not a slide or PRD.

## 2. Real Business Scenario

Imagine a category operator starts work at 9:30 AM.

They do not want to read every chart. They need to answer:

1. Which product category is hurting business performance?
2. Is the issue demand, return, rating, fit, margin, inventory, or PDP content?
3. What are the top three reasons?
4. Did the issue happen recently or has it been persistent?
5. Which orders, SKUs, return reasons, or reviews prove it?
6. Which metric needs drill-down?

So Page 03 should be a **business health monitoring surface**, not a research visualization.

## 3. Core User Questions

### 3.1 For One Product or Category, What Are the Top Three Reasons?

This is one of the most realistic business needs.

For a selected product or category, the page should show:

| Reason Type | Example | Data Source | Business Meaning |
|---|---|---|---|
| Top return reason | Quality Issue, Size Issue, Color Mismatch | Fashion Boutique returns | Why customers return the product |
| Top review pain point | fabric_or_quality, chest_or_bust, length_issue | UCSD fit feedback | What users complain about in text |
| Top operational blocker | high return rate, low rating, low margin | Fashion Boutique KPI layer | Which KPI blocks scale |
| Top size risk | Size 57, Size 38, XL, 2XL | UCSD size metrics, Women Sales size mix | Which size segment may create mismatch |
| Top demand signal | high transaction share, recent order growth | H&M transactions, Women Sales orders | Whether the category deserves attention |

The UI should show this as compact driver chips, not as a paragraph:

```
Selected category: Dress

[Quality Issue 12] [Chest / bust 339] [Return rate 14.8%]
```

Each chip should be clickable:

- Return reason opens return reason details.
- Review pain opens evidence samples.
- KPI blocker opens KPI diagnostics.

### 3.2 What Else Does an Operator Need Beyond Top Three Reasons?

Top three reasons are necessary, but not enough. The operator also needs:

| Need | Why It Matters | Recommended UI |
|---|---|---|
| Recent order momentum | A category may be risky but inactive, or risky and actively selling | Daily/weekly/monthly order trend |
| Latest orders | Operators often inspect recent transactions before changing action | Recent order table |
| SKU concentration | One SKU may create most of the issue | Top SKU table |
| Size mix | Apparel problems often come from size mismatch | Size distribution table or bar |
| Return reason breakdown | One top reason may hide secondary issues | Top 3 return reason table |
| Data confidence | Some categories have connected KPI data, others are model-filled | Coverage badge |
| Ownership signal | Real operation requires follow-up ownership | compact owner/status column |
| Time window | Today's issue and 30-day issue are different | Date range selector |
| Change versus previous period | Operators need trend, not just current value | Delta column |
| Evidence link | Decisions must be auditable | Open evidence button |

## 4. Real Data Already Introduced

The dashboard has new data, and Page 03 should visibly change because of it.

| Dataset | Status | Date Window | Key Fields | Page 03 Usage |
|---|---|---|---|---|
| H&M Personalized Fashion | Connected | 2018-09 to 2020-09 transaction metrics | product group, transaction share, daily transactions | demand proxy and market rhythm |
| UCSD Fit Feedback | Connected | historical review/fit data | category, fit, body type, size, pain point, review text | fit risk, body risk, evidence count |
| Kaggle Women Reviews | Connected | historical review benchmark | class, rating, sentiment | review pressure benchmark |
| Kaggle Fashion Boutique | **Connected in latest build** | 2024-08-06 to 2025-08-06 | category, rating, return rate, return reason, stock, markdown | operating KPI layer |
| Kaggle Women Sales | **Staged in latest build** | 2022-06-01 to 2022-09-09 | order_id, order_date, SKU, size, price, quantity, revenue | recent order module and SKU/size diagnostics |

Important distinction:

- Fashion Boutique has category-level KPI fields, so it can drive Page 03 directly.
- Women Sales has order and SKU fields, but no category field. It should be used for order diagnostics until we map SKU to category.

## 5. Page 03 Main Job

Page 03 should convert mixed data into an operating queue.

It should answer:

| Business Question | Page Component |
|---|---|
| What is the current business condition? | KPI summary strip |
| Which rows are abnormal? | Sortable health table |
| What are the top three drivers? | Top driver chips |
| Is this based on real KPI data? | Data coverage badge |
| What happened recently in orders? | Recent order trend and recent order table |
| What evidence supports the signal? | Evidence preview and drill-down |

## 6. Recommended Page Layout

### 6.1 Overall Structure

```
Header
  Page title: Operations Health
  Date window selector
  Category selector
  Data coverage filter

KPI summary strip
  Active rows
  Connected KPI coverage
  Return pressure
  Recent order revenue
  Evidence-backed rows

Main workspace
  Left: Operations health table
  Right: Selected category detail panel

Lower workspace
  Recent order module
  Top driver module
  Driver breakdown module
```

The page should be dense but readable. Use table, drawer, compact bars, and tabs. Avoid large charts that do not change decisions.

## 7. Top Controls

Every filter must change the table. If a filter does not affect the table, remove it.

| Control | Type | Options | Default | Why |
|---|---|---|---|---|
| Date window | segmented control | 7D, 30D, 90D, MTD, YTD, All | 30D or available latest window | Operators think by time window |
| Category | dropdown | all normalized categories | All categories | Focus work |
| Status | segmented control | All, Healthy, Watch, Risk, Critical | All | Filter business health state |
| KPI blocker | dropdown | All, Return, Rating, Fit, Margin, Demand, Inventory | All | Find problem type |
| Data coverage | segmented control | All, Connected KPI, Model-filled | All | Separate real KPI from estimates |
| Sort | dropdown or table header | Health, Revenue, Orders, Return rate, Evidence, Rating | Health | Control table order |

## 8. KPI Summary Strip

These cards should summarize the current filtered table.

| KPI Card | Definition | Data Source | Click Behavior |
|---|---|---|---|
| Active rows | count of categories or products in current filter | normalized dashboard rows | clears category filter |
| Connected KPI coverage | percent of rows where source is Fashion Boutique | company KPI layer | filter to connected KPI rows |
| Return pressure | count of rows above return threshold | Fashion Boutique or model-fill | filter to high return rows |
| Recent revenue | revenue in selected time window | Women Sales, if mapped or global order module | opens order module |
| Evidence-backed rows | rows with enough review or fit evidence | UCSD, Women Reviews | filter to strong evidence rows |

Copy should be short.

Bad:

> This metric indicates the current operating state of categories and helps the business team understand...

Good:

> 6 categories
> 4 connected KPI
> 2 model-filled

## 9. Main Table: Required Columns

The table is the core of this dashboard.

### 9.1 Recommended Column Set

| Column | Type | Definition | Source | Sort | Filter |
|---|---|---|---|---|---|
| Status | dot / badge | Healthy, Watch, Risk, Critical | computed thresholds | yes | yes |
| Category / Product | text | normalized category or mapped product | merged category model | yes | yes |
| Health score | number | combined operating health index | computed | yes | no |
| Orders | number | order count in selected period | Women Sales when mapped | yes | yes |
| Revenue | currency | revenue in selected period | Women Sales | yes | yes |
| Revenue delta | percent | current period versus previous period | order data | yes | no |
| Units | number | units sold in selected period | Women Sales | yes | no |
| Return rate | percent | returned items divided by products or orders | Fashion Boutique | yes | yes |
| Top return reason | compact chip | most frequent return reason | Fashion Boutique | yes | yes |
| Rating | number | average rating | Fashion Boutique, Women Reviews | yes | yes |
| Fit risk | number | non-fit and size risk | UCSD | yes | yes |
| Top drivers | 3 chips | return reason, review pain, KPI blocker, size issue | merged signals | no | yes |
| Data coverage | badge | Connected KPI, Order-only, Evidence-only, Model-filled | data lineage | yes | yes |
| Evidence | number | review/fit evidence rows | UCSD and reviews | yes | yes |
| Drill-down | icon buttons | evidence, orders, KPI | routing logic | no | no |

### 9.2 Minimum Viable Table

If the page must stay lightweight, start with these columns:

| Column |
|---|
| Status |
| Category |
| Health score |
| Orders |
| Revenue |
| Return rate |
| Top drivers |
| Data coverage |
| Drill-down |

### 9.3 Top Drivers Column

This column is important and should be compact.

Format:

```
[Quality Issue] [Chest / bust] [Return rate]
```

Each item should map to a reason type:

| Reason Type | Example | Source |
|---|---|---|
| Return reason | Quality Issue | Fashion Boutique |
| Review pain | chest_or_bust | UCSD |
| KPI blocker | return rate high | company KPI |
| Demand signal | demand strong | H&M or orders |
| Size signal | XL concentration | Women Sales or UCSD size |

## 10. Selected Category Detail Panel

When a row is selected, show a right-side panel.

### 10.1 Panel Sections

| Section | Content |
|---|---|
| Header | category name, status badge, data coverage |
| Snapshot | opportunity, recent revenue, return rate, fit rate, rating |
| Top drivers | three compact chips with source badge |
| Recent order pulse | latest order date, 7D orders, 30D revenue, top SKU |
| Return reasons | top 3 return reasons |
| Fit and review pain | top 3 semantic or fit issues |
| Drill-down | Evidence, Orders, KPI |

### 10.2 Example Panel

```
Dress
Status: Watch
Coverage: Connected KPI

Top drivers
[Quality Issue 12] [Chest / bust 339] [Return rate 14.8%]

Recent order pulse
Latest order date: 2022-09-09
30D revenue: from order dataset if mapped
Top SKU: 799

Drill-down
[Evidence] [Orders] [KPI]
```

## 11. Order Module

Orders need to become a core part of this dashboard.

The page should show both current category health and recent order behavior.

### 11.1 Why Orders Matter

Without orders, the dashboard is mostly risk analysis. With orders, it becomes operating management.

Orders answer:

- Is this category still selling?
- Did order volume change recently?
- Which SKU drives revenue?
- Which size is overrepresented?
- Is the issue recent or historical?

### 11.2 Time Dimensions

Use multiple time windows because different teams think at different rhythms.

| Window | Meaning | Use Case |
|---|---|---|
| 1D | yesterday or latest available date | daily monitoring |
| 7D | recent operating pulse | short-term anomaly detection |
| 30D | stable recent performance | default operating view |
| MTD | current month to date | monthly business review |
| QTD | current quarter to date | category planning |
| YTD | year to date | annual trend |
| All | full dataset | data context only |

For the current staged Women Sales data:

| Dataset | Date Range | Recommended Use |
|---|---|---|
| Women Sales Orders | 2022-06-01 to 2022-09-09 | daily and weekly order module |
| Fashion Boutique KPI | 2024-08-06 to 2025-08-06 | category KPI and return trend |

Because these two windows are different, the UI must show dataset window labels. Do not imply they are the same live business period.

### 11.3 Order Metrics

| Metric | Formula |
|---|---|
| Orders | count distinct `order_id` |
| Line items | count rows |
| Units | sum `quantity` |
| Revenue | sum `revenue` |
| Average order line revenue | revenue / line items |
| Top SKU | SKU with highest revenue |
| Top size | size with highest units or line items |
| Size missing rate | missing size rows / total rows |
| Recent order delta | current window orders versus previous window orders |

### 11.4 Order Module Layout

Recommended components:

1. **Order pulse card**
   - latest date
   - 7D orders
   - 30D revenue
   - top SKU

2. **Daily order trend**
   - line chart
   - hover shows date, orders, revenue, units
   - supports 7D, 30D, all

3. **Recent orders table**
   - latest 20 order lines
   - columns: order date, order ID, SKU, size, color, unit price, quantity, revenue

4. **SKU and size mix**
   - top SKU table
   - size distribution bar

## 12. Recent Orders Table

This table should exist because it makes the dashboard feel operational.

| Column | Definition | Interaction |
|---|---|---|
| Order date | `order_date` | sort desc |
| Order ID | `order_id` | click to inspect order lines |
| SKU | `sku` | filter to SKU |
| Product/category | mapped category if available | filter |
| Color | `color` | filter |
| Size | `size` | filter |
| Unit price | `unit_price` | sort |
| Quantity | `quantity` | sort |
| Revenue | `revenue` | sort |
| Data source | Women Sales | badge |

If SKU-category mapping is missing, show:

> SKU category not mapped

Do not hide the row. Missing mapping is useful data quality information.

## 13. Driver Breakdown

This module explains why the table ranked a category.

Use a small waterfall or contribution bar.

| Driver | Direction | Meaning |
|---|---|---|
| Demand | positive | category has market signal |
| Recent revenue | positive | orders support attention |
| Return pressure | negative | returns reduce confidence |
| Fit risk | negative | size/fit issue likely |
| Rating pressure | negative | low rating or review issue |
| Margin readiness | positive or negative | margin can or cannot absorb returns |
| Evidence confidence | positive | enough evidence to trust action |

The operator should understand ranking within five seconds.

## 14. Recommended Scoring Model

Use a transparent health model that can be recalculated after new data refresh.

```text
health_score =
  25 * revenue_health
  + 20 * order_momentum
  + 15 * margin_health
  + 15 * rating_health
  + 10 * fit_health
  + 10 * return_health
  + 5  * evidence_confidence
```

Interpretation:

| Score Range | Status | Dashboard Meaning |
|---|---|---|
| 80 to 100 | Healthy | stable operating condition |
| 60 to 79 | Watch | acceptable, monitor drivers |
| 40 to 59 | Risk | visible KPI pressure |
| below 40 | Critical | operating health is weak |

Status should not be text-heavy. Use color and compact labels:

| Status | Color Intent |
|---|---|
| Healthy | green |
| Watch | blue or neutral |
| Risk | amber |
| Critical | red |

## 15. Data Coverage Logic

Every row needs a coverage label.

| Coverage Label | Meaning |
|---|---|
| Connected KPI | category has Fashion Boutique operating KPI |
| Order-only | category has order data but no return/margin KPI |
| Evidence-only | category has review/fit evidence but no order or company KPI |
| Model-filled | missing company KPI, filled by model |

This is critical for trust.

For example:

- `dress`, `top`, `bottom`, `outerwear`, `shoes`, `accessories` can use connected Fashion Boutique KPI.
- `vest`, `tunic`, `culottes`, `frock`, `shirtdress` may be model-filled unless mapped to a connected category.

## 16. Dashboard Modules to Include

### 16.1 Required Modules

| Module | Required | Why |
|---|---|---|
| KPI summary strip | yes | quick operating status |
| Operations health table | yes | core page |
| Selected category panel | yes | drill-down without page jump |
| Top drivers | yes | direct business signal |
| Recent order trend | yes | current business behavior |
| Recent order table | yes | operational evidence |
| Driver breakdown | yes | score explanation |
| Source coverage badge | yes | trust and rigor |

### 16.2 Optional Modules

| Module | Use If |
|---|---|
| Heatmap | useful when SKU-category mapping is complete |
| Cohort by size | useful when order volume is larger |
| Return reason trend | useful when return date exists |
| Inventory risk | useful when stock and sales are both real |
| Forecast | only after stable order data exists |

## 17. What Not to Put on This Page

Do not put:

- abstract relationship graph
- large decorative 3D visualization
- long explanatory paragraphs
- static business story cards
- generic "how to read" text that never changes
- charts that cannot be sorted, filtered, or clicked

Every object should support drill-down, filtering, or comparison.

## 18. Impeccable Design Direction

Using the `impeccable` product UI principles, the page should feel like a serious operating tool:

- restrained dark interface
- table-first layout
- compact KPI cards
- clear filter controls
- no decorative graph canvas
- hover and selected states on rows
- stable typography
- no text overflow
- no mixed language labels
- motion only for state changes

### 18.1 Recommended Visual Hierarchy

1. Page title and date window
2. KPI strip
3. Triage table
4. Detail panel
5. Recent order module
6. Evidence preview

### 18.2 Motion

Use motion only for:

| Motion | Purpose |
|---|---|
| row hover | show clickability |
| drawer update fade | confirm selected row changed |
| sort direction animation | show table resort |
| filter chip active state | show applied filter |

Do not animate table entrance or order trends in a way that slows reading.

## 19. Proposed Page Wireframe

```text
┌────────────────────────────────────────────────────────────────────────────┐
│ 经营看板                         [7D][30D][MTD][YTD] [Category] [Reset] │
├────────────────────────────────────────────────────────────────────────────┤
│ Active rows │ Connected KPI │ Return pressure │ Recent revenue │ Evidence │
├──────────────────────────────────────────────────────────────┬─────────────┤
│ Operations Health Table                                      │ Detail Panel │
│ Status | Category | Health | Orders | Revenue | Return │ Category       │
│        |          |        |        |         | Drivers│ Top drivers    │
│        |          |        |        |         | Source │ KPI snapshot   │
│                                                              │ Drill-down     │
├──────────────────────────────────────────────────────────────┴─────────────┤
│ Driver Breakdown                                                           │
├────────────────────────────────────────────────────────────────────────────┤
│ Recent Orders + SKU/Size Mix                                                │
└────────────────────────────────────────────────────────────────────────────┘
```

## 20. Implementation Data Contract

Build one normalized row per category or product:

```js
{
  id: "dress",
  name: "Dress",
  status: "Watch",
  healthScore: 78.4,
  opportunityIndex: 33.0,
  recentOrders: 42,
  recentRevenue: 12840,
  returnRate: 0.1483,
  topReturnReasons: [
    { reason: "Quality Issue", count: 12 },
    { reason: "Size Issue", count: 7 },
    { reason: "Changed Mind", count: 6 }
  ],
  topReviewPains: [
    { pain: "chest_or_bust", count: 339 },
    { pain: "fabric_or_quality", count: 424 },
    { pain: "color_expectation", count: 310 }
  ],
  fitRisk: 31.2,
  avgRating: 2.529,
  margin: 0.4653,
  dataCoverage: "connected_kpi",
  sources: ["H&M", "UCSD", "Fashion Boutique"]
}
```

The frontend should render from this object. Later, the backend can return the same structure from an API.

## 21. Backend Direction

The dashboard can stay static for MVP, but Page 03 should be designed around a future endpoint:

```text
GET /api/operations-health
  ?window=30d
  &category=all
  &status=all
  &coverage=all
  &sort=health_asc
```

Response:

```json
{
  "updated_at": "2026-06-07T00:00:00Z",
  "window": "30d",
  "rows": [],
  "summary": {},
  "recent_orders": [],
  "source_coverage": {}
}
```

This lets the current CSV frontend migrate to Supabase, PostgreSQL, or another API without redesigning the UI.

## 22. Build Recommendation

Build Page 03 in this order:

1. Replace current Signal Flow with the Operations Health layout.
2. Build `buildOperationsHealthRows()`.
3. Add the sortable table.
4. Add selected category panel.
5. Add order trend and recent orders table.
6. Add top driver logic.
7. Add data coverage badges.
8. Add Chinese and English localization.
9. Validate with local browser and GitHub Pages.

## 23. Acceptance Criteria

Page 03 is acceptable when:

1. It no longer contains relationship graph or signal graph language.
2. The main component is a sortable operations table.
3. A selected row shows top drivers.
4. Recent order metrics are visible.
5. Recent order table exists.
6. Date window controls exist and affect order metrics.
7. Connected KPI versus model-filled coverage is visible.
8. A user can open evidence, orders, and KPI detail from the selected row.
9. Chinese and English both read naturally.
10. The page remains useful after data refresh because it is table-driven, not graph-layout-driven.

## 24. Final Product Principle

The third page should be judged by this question:

> If an operator only has ten minutes, can they understand the business condition and know where to drill down?

If yes, the page works. If it only looks interesting, it fails.
