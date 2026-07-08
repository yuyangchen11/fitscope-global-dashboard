# FitScope Supabase Setup

This directory contains the proposed production database for FitScope Commerce OS.

## What Supabase owns

- Email/password authentication and session refresh
- Password hashing and password reset
- PostgreSQL application data
- Workspace membership and role authorization
- Row Level Security
- Per-user following, alert rules, notifications, and preferences

## What remains server-side

- CSV ingestion and validation
- Alert evaluation jobs
- Any service-role operation
- AI retrieval and model calls

Never place a Supabase secret key or service-role key in the website.

## Setup

1. Create a Supabase project.
2. Enable email/password authentication.
3. Set a password policy and email verification policy.
4. Run migrations in `supabase/migrations` with the Supabase CLI or SQL editor.
5. Create the first user in Supabase Auth.
6. Create one workspace and add the user to `workspace_members` as `admin` or `manager`.
7. Provide the frontend with only:
   - Project URL
   - Publishable key
8. Keep production secrets in Supabase Edge Function secrets or another server environment.

## First workspace example

Replace the user UUID with the UUID shown in Supabase Auth.

```sql
insert into public.workspaces (name, slug)
values ('FitScope Demo', 'fitscope-demo')
returning id;

insert into public.workspace_members (workspace_id, user_id, role)
values ('WORKSPACE_UUID', 'AUTH_USER_UUID', 'manager');
```

## Server-side filtering examples

After authentication, the frontend sends the user's access token. RLS restricts the result to workspaces where that user is a member.

### Orders for a date range and channel

```sql
select id, ordered_at, channel, store_name, status, paid_amount, refund_amount
from public.orders
where workspace_id = 'WORKSPACE_UUID'
  and ordered_at >= '2026-06-01'
  and ordered_at < '2026-07-01'
  and channel = 'Tmall'
order by ordered_at desc
limit 50 offset 0;
```

### SKU drill-down

```sql
select
  ol.sku,
  p.product_name,
  count(distinct ol.order_id) as orders,
  sum(ol.quantity) as units,
  sum(ol.paid_amount) as revenue,
  sum(ol.refund_amount) as refunds
from public.order_lines ol
join public.products p
  on p.workspace_id = ol.workspace_id and p.sku = ol.sku
where ol.workspace_id = 'WORKSPACE_UUID'
  and ol.sku = 'SKU_CODE'
group by ol.sku, p.product_name;
```

### Current user's followed objects

```sql
select entity_type, entity_id, alert_enabled, created_at
from public.followed_entities
where workspace_id = 'WORKSPACE_UUID'
  and user_id = auth.uid()
order by created_at desc;
```

## Frontend integration contract

The login implementation must:

1. Call Supabase Auth with email and password.
2. Load `profiles` and `workspace_members` after a valid session is returned.
3. Derive the workspace navigation from the database role.
4. Query business data with the authenticated JWT.
5. Sign out through Supabase Auth and clear in-memory dashboard state.
6. Never trust a role selected in the browser.

The current management/operator buttons may remain as a demo-preview control on the unauthenticated screen, but the authenticated role must come from `workspace_members`.
