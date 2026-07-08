# Account, Following and Login Specification

## 1. Navigation Model

| Entry | Purpose | Core functions |
|---|---|---|
| Account menu | Short navigation only | Account settings, Following, Switch role, Sign out |
| Account settings | Personal workspace preferences | Language, default page, role, alert preferences |
| Following center | Find saved business objects | Search, type tabs, open object, remove follow |
| Alert center | Review changes requiring attention | Unread count, mark read, open affected object |
| Context star | Save the object currently being inspected | Category, product group, or SKU |

## 2. Following Object Model

Each saved item contains:

- `type`: category, product group, or SKU
- `id`: source identifier
- `label`: localized display name
- `context`: parent product group or category where available
- `targetPage`: page opened from Following
- `followedAt`: timestamp used for recent sorting

Following is stored in browser local storage for the current static version. A production backend should replace it with a user-follow API.

## 3. Account Settings

- Name and email are account identity fields.
- Language changes the entire product.
- Default landing page controls the page opened after login.
- Alert preferences control return, order, and evidence alerts.
- Role switching changes navigation priority and default page.

## 4. Login Page

- One viewport, no vertical scrolling on desktop.
- Left side shows brand and a compact product preview, not marketing copy.
- Right side contains language, identity, role, and sign-in action.
- Chinese and English versions use the same information hierarchy.
