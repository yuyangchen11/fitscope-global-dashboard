begin;

create extension if not exists pgcrypto;

create type public.workspace_role as enum ('admin', 'manager', 'operator');
create type public.follow_entity_type as enum ('category', 'product_group', 'sku');
create type public.action_status as enum ('open', 'in_progress', 'blocked', 'done', 'cancelled');
create type public.notification_severity as enum ('info', 'warning', 'critical');

create table public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  display_name text not null default '',
  language text not null default 'zh' check (language in ('zh', 'en')),
  default_management_page text not null default 'overview',
  default_operator_page text not null default 'operations',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table public.workspaces (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  slug text not null unique,
  created_at timestamptz not null default now()
);

create table public.workspace_members (
  workspace_id uuid not null references public.workspaces(id) on delete cascade,
  user_id uuid not null references auth.users(id) on delete cascade,
  role public.workspace_role not null,
  created_at timestamptz not null default now(),
  primary key (workspace_id, user_id)
);

create table public.product_groups (
  workspace_id uuid not null references public.workspaces(id) on delete cascade,
  id text not null,
  name text not null,
  category_id text,
  active boolean not null default true,
  metadata jsonb not null default '{}'::jsonb,
  primary key (workspace_id, id)
);

create table public.products (
  workspace_id uuid not null references public.workspaces(id) on delete cascade,
  sku text not null,
  product_group_id text,
  category_id text,
  product_name text not null,
  brand text,
  color text,
  size text,
  active boolean not null default true,
  metadata jsonb not null default '{}'::jsonb,
  primary key (workspace_id, sku),
  foreign key (workspace_id, product_group_id)
    references public.product_groups(workspace_id, id)
    on delete set null
);

create table public.orders (
  workspace_id uuid not null references public.workspaces(id) on delete cascade,
  id text not null,
  ordered_at timestamptz not null,
  channel text not null,
  store_name text,
  customer_ref text,
  status text not null,
  currency text not null default 'CNY',
  gross_amount numeric(14,2) not null default 0,
  discount_amount numeric(14,2) not null default 0,
  paid_amount numeric(14,2) not null default 0,
  refund_amount numeric(14,2) not null default 0,
  created_at timestamptz not null default now(),
  primary key (workspace_id, id)
);

create table public.order_lines (
  id bigint generated always as identity primary key,
  workspace_id uuid not null references public.workspaces(id) on delete cascade,
  order_id text not null,
  sku text not null,
  quantity integer not null check (quantity > 0),
  unit_price numeric(14,2) not null,
  paid_amount numeric(14,2) not null,
  refund_amount numeric(14,2) not null default 0,
  fulfillment_status text,
  return_status text,
  return_reason text,
  foreign key (workspace_id, order_id)
    references public.orders(workspace_id, id)
    on delete cascade,
  foreign key (workspace_id, sku)
    references public.products(workspace_id, sku)
);

create table public.reviews (
  id bigint generated always as identity primary key,
  workspace_id uuid not null references public.workspaces(id) on delete cascade,
  sku text,
  category_id text,
  reviewed_at timestamptz,
  rating numeric(3,2),
  fit_label text,
  body_type text,
  occasion text,
  pain_points text[] not null default '{}',
  review_text text not null,
  source text not null,
  foreign key (workspace_id, sku)
    references public.products(workspace_id, sku)
);

create table public.metric_snapshots (
  id bigint generated always as identity primary key,
  workspace_id uuid not null references public.workspaces(id) on delete cascade,
  metric_date date not null,
  entity_type public.follow_entity_type not null,
  entity_id text not null,
  orders integer,
  units integer,
  revenue numeric(14,2),
  conversion_rate numeric(8,6),
  return_rate numeric(8,6),
  margin_rate numeric(8,6),
  rating numeric(4,2),
  fit_rate numeric(8,6),
  source_type text not null,
  source_dataset text,
  confidence numeric(5,4),
  created_at timestamptz not null default now(),
  unique (workspace_id, metric_date, entity_type, entity_id, source_type)
);

create table public.followed_entities (
  id bigint generated always as identity primary key,
  workspace_id uuid not null references public.workspaces(id) on delete cascade,
  user_id uuid not null references auth.users(id) on delete cascade,
  entity_type public.follow_entity_type not null,
  entity_id text not null,
  alert_enabled boolean not null default false,
  created_at timestamptz not null default now(),
  unique (workspace_id, user_id, entity_type, entity_id)
);

create table public.alert_rules (
  id uuid primary key default gen_random_uuid(),
  workspace_id uuid not null references public.workspaces(id) on delete cascade,
  user_id uuid not null references auth.users(id) on delete cascade,
  followed_entity_id bigint not null references public.followed_entities(id) on delete cascade,
  metric_key text not null,
  operator text not null check (operator in ('gt', 'gte', 'lt', 'lte', 'change_pct', 'change_pp')),
  threshold numeric not null,
  lookback_days integer not null default 7 check (lookback_days between 1 and 365),
  enabled boolean not null default true,
  created_at timestamptz not null default now()
);

create table public.notifications (
  id uuid primary key default gen_random_uuid(),
  workspace_id uuid not null references public.workspaces(id) on delete cascade,
  user_id uuid not null references auth.users(id) on delete cascade,
  alert_rule_id uuid references public.alert_rules(id) on delete set null,
  entity_type public.follow_entity_type,
  entity_id text,
  severity public.notification_severity not null default 'info',
  title text not null,
  body text not null,
  payload jsonb not null default '{}'::jsonb,
  read_at timestamptz,
  created_at timestamptz not null default now()
);

create table public.actions (
  id uuid primary key default gen_random_uuid(),
  workspace_id uuid not null references public.workspaces(id) on delete cascade,
  entity_type public.follow_entity_type not null,
  entity_id text not null,
  title text not null,
  reason text,
  owner_id uuid references auth.users(id) on delete set null,
  status public.action_status not null default 'open',
  due_at timestamptz,
  baseline jsonb not null default '{}'::jsonb,
  target jsonb not null default '{}'::jsonb,
  result jsonb not null default '{}'::jsonb,
  created_by uuid not null references auth.users(id),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index orders_workspace_date_idx on public.orders (workspace_id, ordered_at desc);
create index orders_workspace_channel_idx on public.orders (workspace_id, channel, ordered_at desc);
create index order_lines_workspace_sku_idx on public.order_lines (workspace_id, sku);
create index reviews_workspace_sku_idx on public.reviews (workspace_id, sku, reviewed_at desc);
create index metric_snapshots_lookup_idx on public.metric_snapshots (workspace_id, entity_type, entity_id, metric_date desc);
create index notifications_user_unread_idx on public.notifications (user_id, read_at, created_at desc);

create or replace function public.is_workspace_member(target_workspace uuid)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (
    select 1 from public.workspace_members
    where workspace_id = target_workspace and user_id = auth.uid()
  );
$$;

create or replace function public.has_workspace_role(target_workspace uuid, allowed_roles public.workspace_role[])
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (
    select 1 from public.workspace_members
    where workspace_id = target_workspace
      and user_id = auth.uid()
      and role = any(allowed_roles)
  );
$$;

alter table public.profiles enable row level security;
alter table public.workspaces enable row level security;
alter table public.workspace_members enable row level security;
alter table public.product_groups enable row level security;
alter table public.products enable row level security;
alter table public.orders enable row level security;
alter table public.order_lines enable row level security;
alter table public.reviews enable row level security;
alter table public.metric_snapshots enable row level security;
alter table public.followed_entities enable row level security;
alter table public.alert_rules enable row level security;
alter table public.notifications enable row level security;
alter table public.actions enable row level security;

create policy profiles_select_own on public.profiles for select to authenticated using (id = auth.uid());
create policy profiles_update_own on public.profiles for update to authenticated using (id = auth.uid()) with check (id = auth.uid());

create policy workspaces_select_member on public.workspaces for select to authenticated using (public.is_workspace_member(id));
create policy members_select_workspace on public.workspace_members for select to authenticated using (public.is_workspace_member(workspace_id));

create policy product_groups_select_member on public.product_groups for select to authenticated using (public.is_workspace_member(workspace_id));
create policy products_select_member on public.products for select to authenticated using (public.is_workspace_member(workspace_id));
create policy orders_select_member on public.orders for select to authenticated using (public.is_workspace_member(workspace_id));
create policy order_lines_select_member on public.order_lines for select to authenticated using (public.is_workspace_member(workspace_id));
create policy reviews_select_member on public.reviews for select to authenticated using (public.is_workspace_member(workspace_id));
create policy metric_snapshots_select_member on public.metric_snapshots for select to authenticated using (public.is_workspace_member(workspace_id));

create policy follows_select_own on public.followed_entities for select to authenticated using (user_id = auth.uid() and public.is_workspace_member(workspace_id));
create policy follows_insert_own on public.followed_entities for insert to authenticated with check (user_id = auth.uid() and public.is_workspace_member(workspace_id));
create policy follows_update_own on public.followed_entities for update to authenticated using (user_id = auth.uid()) with check (user_id = auth.uid() and public.is_workspace_member(workspace_id));
create policy follows_delete_own on public.followed_entities for delete to authenticated using (user_id = auth.uid());

create policy alert_rules_select_own on public.alert_rules for select to authenticated using (user_id = auth.uid() and public.is_workspace_member(workspace_id));
create policy alert_rules_insert_own on public.alert_rules for insert to authenticated with check (user_id = auth.uid() and public.is_workspace_member(workspace_id));
create policy alert_rules_update_own on public.alert_rules for update to authenticated using (user_id = auth.uid()) with check (user_id = auth.uid());
create policy alert_rules_delete_own on public.alert_rules for delete to authenticated using (user_id = auth.uid());

create policy notifications_select_own on public.notifications for select to authenticated using (user_id = auth.uid());
create policy notifications_update_own on public.notifications for update to authenticated using (user_id = auth.uid()) with check (user_id = auth.uid());

create policy actions_select_member on public.actions for select to authenticated using (public.is_workspace_member(workspace_id));
create policy actions_insert_member on public.actions for insert to authenticated with check (public.is_workspace_member(workspace_id) and created_by = auth.uid());
create policy actions_update_owner_or_manager on public.actions for update to authenticated
using (
  owner_id = auth.uid()
  or public.has_workspace_role(workspace_id, array['admin', 'manager']::public.workspace_role[])
)
with check (public.is_workspace_member(workspace_id));

create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  insert into public.profiles (id, display_name)
  values (new.id, coalesce(new.raw_user_meta_data ->> 'display_name', ''))
  on conflict (id) do nothing;
  return new;
end;
$$;

create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();

commit;
