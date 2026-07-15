# FitScope Commerce OS Product Requirements Document

| Field | Value |
| --- | --- |
| Version | 1.0 |
| Status | Independent study reference build |
| Last updated | 2026-07-15 |
| Product | FitScope Commerce OS |

## 1. Product Summary

FitScope Commerce OS is a bilingual apparel ecommerce operations workspace. It helps management and category operators move from a portfolio-level signal to the affected category, SKU, order line, and review evidence without switching between disconnected reports.

The product does not attempt to replace an order management system. It provides a decision layer over public ecommerce, apparel, fit, and review datasets so that an operator can identify what changed, locate the affected products, inspect supporting records, and decide what to investigate next.

## 2. Problem

Apparel ecommerce decisions are commonly split across sales reports, order tables, assortment files, return analysis, and customer comments. This fragmentation creates four recurring problems:

1. Management can see aggregate KPIs but cannot easily trace a weak result to a category or SKU.
2. Operators can inspect individual orders but lack a consistent way to prioritize which products need attention.
3. Fit and review evidence is disconnected from commercial performance.
4. Static dashboards expose values but do not preserve a usable drill-down path when data changes.

## 3. Target Users

### Management user

Needs a compact view of portfolio performance, category concentration, operating risk, and material changes. The primary task is deciding where attention and operating capacity should be allocated.

### Category operator

Needs category, SKU, order, fulfilment, rating, and review detail. The primary task is finding the product or process driving a change and collecting evidence for follow-up.

## 4. Jobs to Be Done

- When portfolio performance changes, management needs to identify the affected category and understand the size of the impact.
- When a category is selected, an operator needs to rank its products and inspect SKU-level demand, fulfilment, rating, and review signals.
- When a KPI is weak, an operator needs to open the underlying order lines or review samples using the same active filters.
- When an operator is responsible for selected categories or SKUs, they need to follow them and return to them quickly.
- When Chinese- and English-speaking users share the product, each user needs a complete localized workflow rather than a partially translated interface.

## 5. Product Goals and Success Measures

| Goal | Acceptance measure |
| --- | --- |
| Reduce investigation effort | Category-to-SKU or category-to-evidence drill-down is reachable within three interactions. |
| Preserve context | Date, category, product, and role filters remain consistent when opening a related view or drawer. |
| Make visualizations operational | Every primary chart supports hover detail; category and product visuals support selection or drill-down. |
| Support two working modes | Management and operator accounts expose role-appropriate navigation and defaults. |
| Ensure localization | All navigation, controls, states, tooltips, tables, and generated summaries are available in Chinese and English. |
| Maintain desktop usability | No uncontrolled text overflow or horizontal clipping at 1440 px and 1920 px desktop widths. |
| Keep data traceable | Every KPI is mapped to a source table or explicitly identified as derived/modelled. |
| Maintain acceptable performance | Initial desktop view becomes usable within three seconds on a typical broadband connection after assets are cached. |

## 6. Data Model and Business Grain

The product uses five connected grains. Each page must state or imply the grain it is presenting.

| Grain | Business question | Typical identifiers |
| --- | --- | --- |
| Product group/category | Where is demand, assortment, or operating risk concentrated? | product group, category |
| Product/SKU | Which sellable product is driving the result? | product ID, SKU, variant |
| Order | What happened in the customer transaction? | order ID, customer, status, channel, order time |
| Order line | Which product, quantity, and amount contributed to the order? | order-line ID, product ID, quantity, unit price, line revenue |
| Review evidence | What did the customer report about fit, quality, color, or use context? | review ID, product/category, rating, fit label, pain-point tag |

## 7. Information Architecture

The product contains five primary workspaces. Longer pages are preferred over adding pages that do not own a distinct business decision.

| Workspace | Primary user | Decision supported | Core modules |
| --- | --- | --- | --- |
| Overview | Management | Where should attention go? | portfolio KPIs, priority matrix, followed items, change alerts |
| Market & Assortment | Management and operator | Is the assortment aligned with observed demand? | group share, assortment structure, demand comparison, transaction trend |
| KPI & Reviews | Management and operator | Which categories have fit or review risk? | category ranking, risk composition, issue distribution, category filter |
| Product Reviews | Operator | What are customers reporting for the selected category or product? | review KPIs, issue mix, category mix, searchable evidence table |
| Operations | Operator | Which category or SKU needs operational follow-up? | operating health table, SKU drill-down, order trend, order status, payments, order-line table |

## 8. Functional Requirements

### 8.1 Authentication and roles

- Users enter through an explicit submit action; selecting language or role must never log the user in.
- The local server supports manager and operator demo accounts using SQLite-backed sessions.
- GitHub Pages provides a static research preview and must not claim to provide secure production authentication.
- Role selection controls default navigation and permitted workspace visibility.

### 8.2 Global controls

- Language selection is global and persists for the session.
- Date filters support all data, recent periods, and an explicit start/end range where dates exist.
- Category and product selections update dependent KPIs, charts, tables, and drawers.
- Reset restores only the current workspace's filters.
- Followed categories and SKUs are available from the account area and remain visually identifiable in tables.

### 8.3 Overview

- Show a small set of portfolio KPIs with comparison context.
- Rank categories using selectable opportunity, risk, or health measures.
- Selecting a category updates the summary and provides a direct route to operations or evidence.
- Avoid fixed narrative recommendations that would become incorrect after data refresh.

### 8.4 Market & Assortment

- Show product-group structure and share from the active dataset.
- Selecting a treemap block or share segment highlights the same group across the page.
- The selected-group panel shows article count, article share, transaction share, demand gap, and ranks.
- The transaction chart supports time filtering and point-level hover values.
- Unknown or unmapped values are excluded from decision rankings and reported separately in data quality documentation.

### 8.5 KPI & Reviews

- Rank categories by non-fit share, evidence volume, or name.
- Show the components of fit risk using consistent labels and localized tooltips.
- The active category updates all category-dependent metrics.
- Visual labels must remain inside their chart area at supported desktop sizes.

### 8.6 Product Reviews

- Provide category, product, fit, body type, and pain-point filters near the table.
- Keep the result table vertically scrollable so a user can inspect more than a small sample.
- Show issue and category distributions in compact, full-width rows without unused card space.
- Selecting the leading issue applies the corresponding evidence filter.
- Review text is supporting evidence, not a generated recommendation.

### 8.7 Operations

- The operating health table is the primary category-level control surface.
- Users can sort by composite index, sales, orders, rating, and fulfilment.
- Opening a category updates the detail panel and SKU table.
- The SKU table supports search, bounded product selection, sorting, following, and a drill-down drawer.
- Order analysis supports date and product scope, daily/weekly/monthly aggregation, order status, payment method, and line-level inspection.
- Order-line columns include order ID, order time, status, product ID, category, seller/store, region, quantity, unit price, and line revenue when supported by the source.

### 8.8 Drill-down drawer

- The drawer title identifies the selected category, SKU, order, or evidence record.
- It shows the metrics and source records relevant to the element that opened it.
- It preserves the active filters and provides one clear next action.
- It closes by button, Escape key, or backdrop click without losing workspace state.

## 9. Data Sources and Truth Boundaries

| Source | What it supports | Important limitation |
| --- | --- | --- |
| Kaggle Olist | Orders, order items, payments, reviews, sellers, customers, products, fulfilment | Brazilian marketplace data; not a Chinese retailer's internal company data. |
| H&M Personalized Fashion Recommendations | Apparel catalog, product groups, transaction structure | Historical competition data; not live market demand. |
| UCSD Clothing Fit | Fit outcomes, body type, size, and review evidence | Review and fit research data, not company financial data. |
| Women's Clothing Reviews | Rating and review benchmark | Category coverage is narrower than a full marketplace. |
| Boutique samples | SKU/order-line interaction prototypes | Used only where provenance is documented; not a substitute for audited company KPIs. |

Derived metrics must be reproducible from committed processed files. Values that cannot be supported by a source must be removed from production-facing views or labelled as modelled in documentation, not inside the final interface.

## 10. Technical Approach

- Frontend: a static HTML/CSS/JavaScript dashboard that loads processed CSV assets.
- Local authentication: Python standard-library server with SQLite sessions.
- Public preview: GitHub Pages with static fallback behavior.
- Data refresh: source-specific processing scripts rebuild processed CSVs without requiring layout changes.
- Future production path: replace CSV fetches with a database/API adapter while retaining the same normalized view models.

## 11. Non-Functional Requirements

- Desktop-first support for 1440 px and 1920 px viewports.
- Keyboard-operable login, language controls, menus, tables, and drawers.
- Visible focus states and sufficient contrast for controls and data labels.
- Reduced-motion preference disables nonessential background animation.
- Large option lists use bounded, searchable popovers rather than unbounded native menus.
- Tables use sticky headers and independent vertical scrolling where record volume is high.
- Data-loading failures provide a recovery action and do not leave a blank page.

## 12. Out of Scope

- Replacing an OMS, CRM, ERP, or customer service platform.
- Production payment, refund, or inventory write operations.
- Claiming live Chinese-market demand without a licensed or current source.
- Autonomous AI actions or unreviewed recommendations.
- Mobile optimization for the current independent-study release.

## 13. Risks and Mitigations

| Risk | Mitigation |
| --- | --- |
| Public datasets represent different businesses and periods | Keep source boundaries visible in documentation and avoid unsupported joins. |
| Static hosting cannot provide secure login | Treat GitHub Pages as a preview; use the local/server deployment for authenticated sessions. |
| Generated text becomes stale after refresh | Prefer metrics, rules, filters, and source evidence over fixed recommendations. |
| Long category or SKU lists damage usability | Use search, result limits, scrolling, and explicit all-category states. |
| Partial localization causes incorrect workflows | Maintain all dynamic labels in the shared i18n dictionaries and test both languages. |

## 14. Release Acceptance Checklist

- Login stays on the login page until the user submits the form.
- Switching language or role does not trigger authentication.
- Both roles can enter their intended workspace using the documented demo accounts.
- Product scope remains bounded and searchable with large SKU lists.
- Review distributions fill their cards without unnecessary empty regions.
- Every primary chart has hover detail and every selectable visualization has a visible selected state.
- Date filtering updates every time-dependent module on the active workspace.
- Chinese and English views contain no mixed-language control states.
- No chart label, table control, or account control overflows at 1440 px and 1920 px.
- The README links to this PRD, data catalog, column dictionary, deployment guide, and public website.

## 15. Delivery Phases

1. Research release: committed public data, five workspaces, bilingual UI, drill-down interactions, and local role-based login.
2. Data-service release: database/API adapter, scheduled refresh, source health, and stronger authorization.
3. Operating release: organization-specific KPIs, alert subscriptions, action ownership, and validated AI-assisted summaries.
