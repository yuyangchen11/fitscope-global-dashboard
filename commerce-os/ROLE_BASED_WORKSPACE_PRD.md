---
artifact: prd
version: "0.1"
created: 2026-06-26
status: draft
---

# PRD: Role-Based FitScope Commerce OS Workspace

## 1. Overview

### Problem Statement
FitScope Commerce OS already connects market, operations, KPI, order, fit, and review evidence into one dashboard. The next product problem is role clarity: a manager and an operator should not enter the same workspace with the same information priority.

Managers need to judge category direction, resource allocation, and KPI risk quickly. Operators need to find the exact category, SKU, order, review, or action item that needs work today. If both roles see the same first screen, the dashboard becomes either too abstract for execution or too detailed for management.

### Solution Summary
Add role-based entry logic after login:

- **Management view**: opens an executive workspace focused on category portfolio, KPI health, market opportunity, risk exposure, and decision priority.
- **Operator view**: opens an execution workspace focused on daily operating table, order lines, evidence filters, top issue drivers, and action follow-up.

V1 should use the same underlying data and pages, but change default landing page, KPI priority, visible modules, filters, and action wording by role.

### Target Users

| User | Primary Job | Decision Level | Dashboard Need |
|---|---|---:|---|
| Management | Decide which categories to scale, pause, or fix | Portfolio / weekly | Fast risk and opportunity read |
| Operator | Execute PDP, sizing, SKU, evidence, and order checks | Category / daily | Detailed queue and drill-down evidence |
| Tutor / Reviewer | Evaluate project rigor and data-product completeness | Academic / review | Clear product logic, data traceability, and realistic workflow |

## 2. Goals and Success Metrics

### Goals

1. Make role selection meaningful, not just a label change.
2. Reduce cognitive load by showing the most relevant page and modules first.
3. Preserve one shared data model so the project remains maintainable.
4. Support bilingual users with role-specific Chinese and English copy.

### Success Metrics

| Metric | Baseline | V1 Target | Notes |
|---|---:|---:|---|
| Time to first useful decision | Unknown | < 30 seconds in usability test | User can identify next action without explanation |
| Role-specific landing accuracy | 0% | 100% | Selected role opens correct default workspace |
| Redundant module exposure | High | Reduced | Hide or de-emphasize modules irrelevant to role |
| Drill-down completion | Partial | User can go from KPI/category to evidence/order detail | Critical for operator workflow |
| Bilingual completion | Partial | All role-specific labels localized | Chinese-only and English-only users both usable |

### Non-Goals

- Do not build real authentication or permission enforcement in V1.
- Do not create two separate products or duplicate dashboards.
- Do not fabricate company-level data that looks like real production data unless clearly modeled or derived.
- Do not make the manager view text-heavy. It should remain dashboard-first.

## 3. Role Model

### Management View

Default landing page: **Overview**

Primary questions:

- Which category deserves attention this week?
- Is the issue market opportunity, operating risk, margin, return, or evidence quality?
- Which categories should scale, validate, watch, or fix?
- Where should the team spend effort next?

Core modules:

| Module | Purpose | Display Logic |
|---|---|---|
| Executive KPI row | Show GMV/revenue, conversion, return, margin, health | Aggregate or selected time range |
| Priority Matrix | Rank categories by opportunity, risk, and health | Sortable by opportunity/risk/health |
| Category Status | Show top categories and action status | Click category to sync workspace |
| Market & Assortment Summary | Show product group demand and concentration | High-level only |
| Weekly Operating Path | Show market -> operations -> evidence workflow | Compact, no long explanations |

What management should not see first:

- Full review text table.
- Long order-line table.
- Raw data-source labels such as CSV.
- Detailed SKU rows unless drilled down.

### Operator View

Default landing page: **Operations**

Primary questions:

- Which category or SKU needs work today?
- What are the top three drivers behind the issue?
- Which order lines or review samples support the issue?
- What concrete action should be taken and tracked?

Core modules:

| Module | Purpose | Display Logic |
|---|---|---|
| Operating Health Table | Main working table for category triage | Sort and filter by health, revenue, return, rating |
| Category Detail Panel | Show selected category metrics and top drivers | Updates on row click |
| Order Line Detail | Inspect item-level transaction evidence | Search, date range, channel, type, size filters |
| Evidence Table | Inspect fit/review evidence | Search, category, fit, body type, pain point filters |
| Action Cards | Convert diagnosis into execution tasks | Based on selected category and top drivers |

What operators should not see first:

- Executive story blocks.
- Broad market summaries without direct action.
- Abstract relationship graph.
- Static explanation text that does not update with filters.

## 4. Functional Requirements

### FR-1: Role Selection

- User can choose Management view or Operator view on login.
- Selected role is stored in front-end state.
- Current role is visible in the sidebar.
- Switching language must preserve selected role.

### FR-2: Role-Based Default Landing

- Management login opens Overview.
- Operator login opens Operations.
- If the user manually navigates, role should not forcibly redirect.

### FR-3: Role-Based Navigation Priority

- Management nav order: Overview, Market & Assortment, KPI & Semantics, Operations, Actions & Evidence.
- Operator nav order: Operations, Actions & Evidence, KPI & Semantics, Market & Assortment, Overview.
- V1 can keep all pages visible, but order and default page should differ.

### FR-4: Role-Based Module Emphasis

- Management view should emphasize aggregate KPI cards, category priority, and portfolio decisions.
- Operator view should emphasize tables, filters, drawers, orders, review evidence, and action tracking.
- Shared modules can remain, but the first viewport should be role-specific.

### FR-5: Drill-Down Continuity

- Clicking a category in management view should open the selected category in Operations or Market context.
- Clicking an operator row should open the drawer or update the right-side detail panel.
- Date range and category filters should remain consistent when moving between relevant pages.

### FR-6: Localization

- All role labels, navigation names, button text, and module titles must support Chinese and English.
- Avoid literal translation when business wording should differ by role.

## 5. Data Requirements

V1 uses existing local/public datasets:

| Data Layer | Source | Role Usage |
|---|---|---|
| Market assortment | H&M public articles / transactions | Management portfolio and market page |
| Transaction sample | H&M transactions sample | Operator order detail and time filters |
| Company operating KPI | Fashion boutique / sales datasets where available, otherwise marked modeled | Management KPI health |
| Fit and review evidence | UCSD + women reviews | Operator evidence and semantic diagnosis |
| Return and issue drivers | Derived metrics | Both roles, with different display depth |

Future database direction:

- Keep `data/*.csv` as the current ingestion layer.
- Add a replaceable API layer later: `/api/metrics`, `/api/orders`, `/api/evidence`, `/api/actions`.
- Keep front-end modules consuming normalized objects, not raw CSV columns.

## 6. UX Design Principles

1. **One role, one first question.** Management starts with portfolio direction; operator starts with execution queue.
2. **Dashboard first, prose second.** Use tables, KPI cards, rank lists, and drill-downs instead of long explanatory text.
3. **Every click should change context.** Clicking a category, row, chart, or KPI should update detail, drawer, or navigation.
4. **Keep data caveats visible but quiet.** Do not show labels like CSV as primary content.
5. **Bilingual without clutter.** Chinese and English should both fit in one line where possible.

## 7. V1 Scope

### In Scope

- Role-aware login state.
- Role-specific default page.
- Role-specific nav order or visual priority.
- Management and Operator copy localization.
- Role-specific first-viewport module emphasis.
- Category click continuity from management to operator detail.

### Out of Scope

- Real login authentication.
- Backend permission model.
- User account management.
- Role-based data access security.
- Real-time collaboration or assignment workflow.

### Future Considerations

- Action ownership, due dates, and status history.
- Saved views per role.
- AI assistant that explains selected category or drafts PDP action notes.
- Backend database/API replacement for static CSV ingestion.
- Exportable weekly business review report.

## 8. Risks and Mitigation

| Risk | Likelihood | Impact | Mitigation |
|---|---:|---:|---|
| Role split adds complexity without value | Medium | High | Start with default landing and module priority, not separate products |
| Data is not deep enough for operator workflow | Medium | High | Use order/evidence drill-down where available, mark derived metrics clearly |
| Text becomes too role-specific and brittle | Medium | Medium | Prefer metric labels and table states over paragraph recommendations |
| English/Chinese layout breaks | Medium | Medium | Test both languages on all pages after every UI change |

## 9. Milestones

| Milestone | Output |
|---|---|
| M1: Role Definition | Finalize manager/operator jobs, modules, and nav order |
| M2: Front-End Role State | Login role controls default page and sidebar label |
| M3: Role-Specific First View | Management overview and operator operations page differ meaningfully |
| M4: Drill-Down Flow | Category -> operations -> evidence/order detail works smoothly |
| M5: QA | Chinese/English, 1440x900, mobile, no overflow, no dead clicks |

## 10. Open Questions

- Should Operator be called “运营视角” or “执行视角” in Chinese? Recommendation: “运营视角,” because it sounds closer to ecommerce work.
- Should management still see Evidence in nav? Recommendation: yes, but lower priority.
- Should operator see Overview? Recommendation: yes, but lower priority or read-only.
- Should role selection be switchable inside the app? Recommendation: V1 yes, but as a small control in sidebar or profile menu.
