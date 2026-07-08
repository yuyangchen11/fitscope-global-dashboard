# Deployment and Sharing

## Public reviewer link

GitHub Pages should serve the static dashboard at:

https://yuyangchen11.github.io/fitscope-global-dashboard/

This link works for advisors and teammates without being on the same Wi-Fi network.

## Local authenticated demo

Run from the repository root:

```bash
python3 server.py --port 4182
```

Open:

```text
http://127.0.0.1:4182/commerce-os/index.html
```

The local server supports the demo login flow and redirects common wrong paths such as `/site/commerce-os/index.html` to the correct route.

## Why CSV is not zipped

The frontend loads dashboard data with browser `fetch()` calls. Keeping processed data as plain CSV makes the website portable and auditable. Zip files are only appropriate for archived raw datasets that are not fetched directly by the dashboard.
