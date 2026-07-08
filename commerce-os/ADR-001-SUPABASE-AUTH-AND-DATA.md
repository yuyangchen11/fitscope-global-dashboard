---
artifact: adr
version: "1.0"
created: 2026-06-30
status: proposed
---

# ADR-001: Use Supabase Auth and PostgreSQL

## Status

Proposed

**Date:** 2026-06-30  
**Deciders:** Independent Study project team

## Context

FitScope Commerce OS is currently a static GitHub Pages application. Login is only a client-side screen, role switching is not authorization, and business data is loaded from browser-accessible CSV files. The next version needs real accounts, role-scoped access, per-user following, persistent notifications, and server-side filtering without requiring the team to operate a custom authentication service.

The project must remain easy to deploy and accessible to mentors outside the local network. Private operating data must not be bundled into the public website.

## Decision

We will use Supabase Auth for email/password sessions and a Supabase-hosted PostgreSQL database for application and operating data.

We will:

1. Keep the frontend deployable as a static site.
2. Authenticate users through Supabase Auth.
3. Store workspace membership and roles in database tables, not editable user metadata.
4. enforce authorization with PostgreSQL Row Level Security.
5. Store following, alert rules, notifications, preferences, actions, products, orders, order lines, reviews, and metric snapshots in PostgreSQL.
6. Query filtered and paginated rows from the database instead of downloading complete private CSV files.
7. Use the browser-safe Supabase publishable key in the frontend.
8. Keep service-role or secret keys only in server-side ingestion jobs or Edge Functions.
9. Retain public CSV files only as development/demo sources until their ingestion is migrated.

## Consequences

### Positive

- Password hashing, sessions, password reset, and token refresh are handled by an established auth service.
- PostgreSQL supports the relational joins and analytical filtering required by orders, SKUs, reviews, and actions.
- Row Level Security can restrict every query by authenticated user and workspace.
- The existing static site can remain on GitHub Pages during the transition.
- Following and preferences become portable across devices instead of being tied to localStorage.

### Negative

- The project gains an external service dependency.
- RLS policies must be tested carefully; a permissive policy can expose data.
- Large analytical workloads may eventually need materialized views, scheduled aggregation, or a warehouse.
- Real-time and background alerts require a scheduled job or Edge Function, not only database tables.

### Neutral

- GitHub Pages remains a frontend host, not an application backend.
- Public demonstration data and private operating data will follow different ingestion and access paths.

## Alternatives Considered

### Firebase Authentication and Firestore

Strong managed authentication and security rules, but the document model is less natural for order lines, SKU/category joins, metric windows, and SQL-style analysis.

### Custom Node.js API and PostgreSQL

Provides maximum control, but requires server hosting, password/session implementation, deployment, monitoring, and more maintenance than the study needs.

### Auth0 or Clerk plus a separate database

Strong identity products, but introduces two vendors and a separate database integration. It is better suited when enterprise SSO or advanced identity requirements dominate the project.

### Continue with localStorage and CSV

Rejected for production use because it cannot enforce identity, roles, per-user data isolation, or private-data access.

## References

- Supabase Auth documentation: https://supabase.com/docs/guides/auth
- Supabase data security documentation: https://supabase.com/docs/guides/database/secure-data
- FitScope audit: `DASHBOARD_AUDIT_2026-06-30.md`
- Role workspace PRD: `ROLE_BASED_WORKSPACE_PRD.md`
