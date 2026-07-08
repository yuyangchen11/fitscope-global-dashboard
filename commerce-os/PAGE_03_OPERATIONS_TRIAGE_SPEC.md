# Page 03 Redesign: Category Operations Triage

## Decision

Page 03 should stop being a relationship graph or signal graph.

For an operator, the most valuable question is not "how are nodes connected?" The real question is:

> Which category needs action today, why, what should I do first, and what evidence supports it?

The page should become a **Category Operations Triage** workspace: a lightweight, sortable, filterable operating table with focused KPI diagnostics and evidence drill-down.

Recommended navigation label:

| Language | Current | Recommended |
|---|---|---|
| Chinese | 信号流 | 运营诊断 |
| English | Signal Flow | Operations Triage |

## Why the Current Page Is Not Good Enough

The current "Signal Flow" page still feels like a relationship graph concept even after visual changes. It has three problems:

1. **Weak operator value**: Operators do not need to inspect abstract graph nodes. They need ranked work, blockers, evidence, and next actions.
2. **Poor scalability**: When real data changes daily, graph layouts become unstable and hard to compare. Tables and ranked diagnostics handle changing data better.
3. **Duplicated purpose**: KPI, pain point, action, and evidence are already elsewhere. Page 03 should not repeat those views as a diagram. It should coordinate them into an operational queue.

## Target User

Primary user: category operator, ecommerce operation analyst, merchandising analyst.

They use this page to:

- Find categories that need intervention.
- Understand whether the blocker is demand, return, rating, fit, margin, size, or content.
- Open the right evidence without manually switching pages.
- Decide whether to scale, fix, observe, or pause.

Secondary user: manager.

They use this page to:

- Check whether the team's action queue is data-backed.
- See which categories have real KPI coverage versus model-filled estimates.
- Challenge recommendations when evidence is thin.

## Role in the Dashboard

The redesigned Page 03 should sit between market discovery and evidence/action execution.

| Page | Role |
|---|---|
| 01 Overview | Executive snapshot: current opportunity, risk, and top queue |
| 02 Market & Assortment | Market demand, assortment structure, transaction momentum |
| **03 Operations Triage** | **Rank category work, explain blockers, route to evidence/actions** |
| 04 KPI & Semantics | Deeper KPI and semantic diagnosis |
| 05 Tasks & Feedback | Review samples and product-task checklist |

## Real Data Status

Real or semi-real data has been introduced, but the dashboard should change to use it more explicitly.

| Data Source | Current Status | Useful Fields | Current Use | Needed Page 03 Use |
|---|---|---|---|---|
| H&M Personalized Fashion | Connected | product group, transactions, daily trend | market demand and assortment proxy | demand share, transaction signal, category scale |
| UCSD Fit Feedback | Connected | category, fit, body type, size, pain point | fit risk and evidence | fit risk, body/size blocker, evidence count |
| Kaggle Women Reviews | Connected | class, rating, sentiment metrics | review benchmark | rating pressure and semantic benchmark |
| Kaggle Fashion Boutique | **Newly connected** | category, rating, return rate, return reason, markdown, stock | operating KPI layer for covered categories | return reason, operating readiness, data coverage badge |
| Kaggle Women Sales | **Newly staged** | order date, SKU, size, price, quantity, revenue | not yet primary page input | SKU/order validation, size mix, sales rhythm if mapped |

Important:

- `kaggle_fashion_boutique_company_category_kpi.csv` is already loaded by the frontend as `companyKpis`.
- Categories covered by this dataset should show `Real KPI proxy` or `Connected KPI` status.
- Categories not covered should show `Model-filled` status.
- This distinction must be visible because operators should not trust every recommendation equally.

## Page Objective

Page 03 should answer five questions in one workflow:

1. **What should I work on first?**
2. **Why is it ranked there?**
3. **Which KPI is blocking action?**
4. **Is the evidence real, proxy, or model-filled?**
5. **Where do I go next?**

## Proposed Layout

### 1. Top Control Bar

Purpose: let the operator scope the triage queue.

Controls:

| Control | Type | Why It Exists |
|---|---|---|
| Category group | multi-select or dropdown | Focus on one group without losing table context |
| Action type | segmented control | Show Scale, Fix returns, Fix PDP, Validate, Watch |
| KPI blocker | dropdown | Filter by return, conversion, margin, fit, rating, demand |
| Data coverage | toggle | Show all, connected KPI only, model-filled only |
| Reset | button | Return to default ranked queue |

Remove global filters that do not affect the current page. Every filter on this page must update the triage table.

### 2. KPI Summary Strip

Purpose: summarize the current filtered queue, not repeat generic dashboard KPIs.

Recommended cards:

| Card | Definition | Why It Matters |
|---|---|---|
| Actionable categories | count of categories with Scale/Fix/Validate action | Shows workload size |
| Connected KPI coverage | share of rows with real/proxy company KPI | Shows confidence level |
| Return-pressure categories | count above return threshold | Shows operational risk |
| Evidence-backed rows | share with review/fit evidence count above minimum | Prevents acting on thin evidence |

Design:

- Compact cards, one line title, one number, one short secondary metric.
- No long explanatory paragraph.
- Cards are clickable and filter the table.

### 3. Main Module: Operations Triage Table

This should be the core of the page.

Why table instead of graph:

- Operators compare categories row by row.
- Sorting and filtering are more useful than spatial layout.
- Tables remain stable when new data arrives.
- Drill-down can be explicit and auditable.

Recommended columns:

| Column | Source | Interaction |
|---|---|---|
| Rank | computed | sort by priority |
| Category | normalized category | click opens category drawer |
| Recommended action | decision rule | filterable badge |
| Opportunity index | H&M + demand proxy | sortable |
| Return rate | Fashion Boutique if covered, else model-filled | sortable, badge by source |
| Top return reason | Fashion Boutique return reason | filterable |
| Fit risk | UCSD fit feedback | sortable |
| Rating / review pressure | Kaggle Women Reviews or Fashion Boutique rating | sortable |
| Evidence volume | UCSD evidence count + review count | sortable |
| Data coverage | connected KPI / proxy / model-filled | filterable |
| Next step | generated action | button: View reviews, Open tasks, Open KPI |

Default sort:

`priority_score desc`

Priority score should be transparent:

```
priority_score =
  opportunity_weight
  + return_pressure_weight
  + fit_risk_weight
  + rating_pressure_weight
  - readiness_penalty
  + evidence_confidence_weight
```

The page should show the formula only as a small "Scoring rule" drawer, not as large text cards.

### 4. Category Detail Drawer

Purpose: avoid opening a full page for every click.

When the user clicks a table row, open a right-side drawer with:

| Section | Content |
|---|---|
| Category snapshot | demand index, return rate, fit rate, rating, evidence count |
| Main blocker | one KPI or semantic reason |
| Data confidence | connected KPI / proxy / model-filled, with source files |
| Top return reasons | mini table from `kaggle_fashion_boutique_return_reason_metrics.csv` |
| Top fit/semantic pain | mini table from UCSD pain metrics |
| Action checklist | 3 to 5 operational tasks |
| Navigation | View reviews, Open tasks, Open KPI details |

This drawer replaces the current "Signal Inspector".

### 5. Driver Breakdown

Purpose: explain ranking without long text.

Use a compact stacked bar or waterfall per selected category:

| Driver | Example |
|---|---|
| Demand contribution | positive |
| Return pressure | negative |
| Fit risk | negative |
| Rating pressure | negative |
| Margin/readiness | positive or negative |
| Evidence confidence | positive if enough evidence |

This answers: "Why is this category ranked here?"

### 6. Return Reason and Evidence Preview

Purpose: use newly introduced real operating data.

Recommended module:

| Tab | Content |
|---|---|
| Return reasons | reason, count, category share |
| Review pain | pain tag, mentions, sample count |
| Size risk | size, risk score, eligible display |
| SKU/order signal | if available, top SKU, size mix, revenue |

Do not show long paragraphs by default.

Show only tables and short labels. Long comments should stay in Page 05.

## Interaction Model

### Default Load

1. Load all data.
2. Build normalized category rows.
3. Merge company KPI rows from Fashion Boutique.
4. Mark each row with `data_coverage`.
5. Sort by `priority_score`.
6. Show the top 12 rows in the table.
7. Auto-select the first row in the drawer.

### Clicking a KPI Card

Clicking "Return-pressure categories" filters the table to high-return rows.

Clicking "Connected KPI coverage" filters to rows where `source = kaggle_fashion_boutique`.

Clicking "Evidence-backed rows" filters to rows with enough UCSD/review samples.

### Clicking a Table Row

Updates:

- category drawer
- driver breakdown
- return reason/evidence preview
- top control selected category

It should not jump to another page unless the user clicks a navigation button.

### Clicking "Open Evidence"

Navigate to Page 05 with filters pre-applied:

- selected category
- selected pain point or return reason if available
- evidence table scrolled into view

### Clicking "Open Actions"

Navigate to Page 05 action cards, preserving selected category.

## Data Model for Page 03

The page should use a normalized object like:

```js
{
  category: "dress",
  displayName: "Dress",
  opportunityIndex: 33.0,
  demandShare: 0.395,
  conversion: 0.0514,
  returnRate: 0.1483,
  margin: 0.4653,
  avgRating: 2.529,
  topReturnReason: "Quality Issue",
  fitRate: 0.741,
  nonFitRate: 0.259,
  riskScore: 31.2,
  topPainPoint: "chest_or_bust",
  evidenceRows: 167140,
  dataCoverage: "connected_kpi",
  source: ["H&M", "UCSD", "Fashion Boutique"],
  recommendedAction: "Validate",
  priorityScore: 82.4
}
```

This is the page contract. The UI should not care whether the object came from static CSV, Supabase, PostgreSQL, or an API.

## Backend / Database Direction

The page should be designed as if it will later read from one endpoint:

```
GET /api/category-triage?category=&action=&coverage=&blocker=
```

Expected response:

```json
{
  "updated_at": "2026-06-07T00:00:00Z",
  "rows": [],
  "summary": {},
  "source_coverage": {}
}
```

Current static MVP can simulate this endpoint by building the same object in browser memory.

## Visual Style

Use the current dark product shell, but simplify Page 03:

- Fewer cards.
- More table density.
- Less decorative motion.
- No graph canvas.
- No node layout.
- No large explanatory paragraphs.
- Strong hover states for rows and drawer actions.
- Clear source badges: `Connected KPI`, `Proxy`, `Model-filled`.

Recommended structure:

```
Header
Controls
Summary KPI strip
Main split:
  Left 70%: Operations triage table
  Right 30%: Category drawer
Bottom:
  Driver breakdown
  Return reason / review pain preview
```

## Localization Requirements

Chinese and English must both be complete.

Rules:

- Do not show mixed labels like `胸围/胸部 · chest_or_bust` unless intentionally in evidence/debug mode.
- For user-facing UI, show localized label first.
- Put raw data code in tooltip or small secondary text only if useful.
- Column headers, badges, filters, drawer labels, action buttons, and empty states must all use i18n.

## What Should Be Removed From Current Page

Remove:

- `Category Signal Flow` as a visual concept.
- `Operating Signals` node list.
- `Signal Inspector`.
- Graph filter buttons: All, Risk, Action, KPI.
- Any relationship/node wording.

Replace with:

- Triage table.
- Category drawer.
- Driver breakdown.
- Return reason and evidence preview.

## Acceptance Criteria

1. Page 03 default view shows a ranked table, not a graph.
2. Every row has a visible data coverage label.
3. The table supports sorting by priority, return rate, opportunity, fit risk, evidence volume, and rating.
4. The page uses `kaggle_fashion_boutique_company_category_kpi.csv` when category coverage exists.
5. Categories without connected KPI data are visibly marked as model-filled.
6. Clicking a row updates the drawer without page navigation.
7. Clicking Open Evidence navigates to Page 05 with filters applied.
8. Chinese and English modes show no mixed-language UI labels.
9. The page remains useful if tomorrow's data changes ranking, category coverage, or top return reasons.
10. No text overflows buttons, cards, table cells, or drawer panels at desktop and tablet widths.

## Implementation Plan

### Stage 1: Data Contract

Create a `buildTriageRows()` function that merges:

- H&M demand metrics
- UCSD fit and pain metrics
- Fashion Boutique company KPI metrics
- review benchmark metrics

Output normalized rows with `dataCoverage`.

### Stage 2: Replace Page 03 DOM

Replace current network/signal section with:

- summary strip
- table container
- drawer container
- driver breakdown
- evidence preview tabs

### Stage 3: Interactions

Add:

- sort state
- filter state
- selected row state
- row click drawer update
- evidence/action navigation

### Stage 4: Localization

Add i18n keys for:

- page label
- table headers
- sort controls
- coverage badges
- drawer labels
- empty states

### Stage 5: QA

Verify:

- local CSV loading
- GitHub Pages CSV loading
- Chinese mode
- English mode
- no overflow
- no stale graph wording
- real KPI rows appear with connected coverage

## Recommended Next Build Decision

Build this page before adding more charts.

Reason: the dashboard already has enough charts. What is missing is an operational workbench that turns the data into a credible queue. A table-driven triage page will make the product feel more professional and easier to defend to a professor or business stakeholder.
