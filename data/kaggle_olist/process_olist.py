#!/usr/bin/env python3
"""Build browser-sized, traceable metrics from the real Olist dataset."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RAW = ROOT / "raw"
PROCESSED = ROOT / "processed"
PROCESSED.mkdir(parents=True, exist_ok=True)


def read_csv(name: str):
    with (RAW / name).open(encoding="utf-8-sig", newline="") as handle:
        yield from csv.DictReader(handle)


def parse_dt(value: str):
    if not value:
        return None
    return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")


def write_csv(name: str, rows: list[dict], fields: list[str]):
    with (PROCESSED / name).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def ratio(numerator: float, denominator: float):
    return round(numerator / denominator, 6) if denominator else 0


translations = {
    row["product_category_name"]: row["product_category_name_english"]
    for row in read_csv("product_category_name_translation.csv")
}
translations["fashion_roupa_feminina"] = "fashion_female_clothing"

products = {}
for row in read_csv("olist_products_dataset.csv"):
    category_pt = row["product_category_name"] or "unclassified"
    category = translations.get(category_pt, category_pt)
    products[row["product_id"]] = {
        "category": category,
        "category_pt": category_pt,
        "photos": row["product_photos_qty"],
        "weight_g": row["product_weight_g"],
    }

orders = {row["order_id"]: row for row in read_csv("olist_orders_dataset.csv")}
customers = {row["customer_id"]: row for row in read_csv("olist_customers_dataset.csv")}

reviews_by_order = defaultdict(list)
for row in read_csv("olist_order_reviews_dataset.csv"):
    if row["review_score"]:
        reviews_by_order[row["order_id"]].append(float(row["review_score"]))

payments_by_order = defaultdict(list)
for row in read_csv("olist_order_payments_dataset.csv"):
    payments_by_order[row["order_id"]].append(row)

fashion_categories = {
    "fashion_bags_accessories",
    "fashion_shoes",
    "fashion_male_clothing",
    "fashion_female_clothing",
    "fashion_underwear_beach",
    "fashion_sport",
    "fashion_childrens_clothes",
}

category_stats = defaultdict(lambda: {
    "orders": set(), "products": set(), "sellers": set(), "customers": set(),
    "units": 0, "revenue": 0.0, "freight": 0.0, "review_sum": 0.0,
    "review_count": 0, "delivered": 0, "on_time": 0, "late": 0,
    "cancelled": 0, "latest_order": "",
})
product_stats = defaultdict(lambda: {
    "orders": set(), "sellers": set(), "units": 0, "revenue": 0.0,
    "freight": 0.0, "review_sum": 0.0, "review_count": 0,
    "delivered": 0, "on_time": 0, "latest_order": "",
})
daily_stats = defaultdict(lambda: {
    "orders": set(), "units": 0, "revenue": 0.0, "freight": 0.0,
    "review_sum": 0.0, "review_count": 0, "delivered": 0, "on_time": 0,
})
order_totals = defaultdict(lambda: {"revenue": 0.0, "freight": 0.0, "units": 0})
order_lines = []

for row in read_csv("olist_order_items_dataset.csv"):
    order = orders.get(row["order_id"], {})
    product = products.get(row["product_id"], {"category": "unclassified", "category_pt": "unclassified"})
    category = product["category"]
    purchase_at = parse_dt(order.get("order_purchase_timestamp", ""))
    delivered_at = parse_dt(order.get("order_delivered_customer_date", ""))
    estimated_at = parse_dt(order.get("order_estimated_delivery_date", ""))
    date = purchase_at.date().isoformat() if purchase_at else ""
    price = float(row["price"] or 0)
    freight = float(row["freight_value"] or 0)
    status = order.get("order_status", "unknown")
    review_scores = reviews_by_order.get(row["order_id"], [])
    review_score = sum(review_scores) / len(review_scores) if review_scores else 0
    customer = customers.get(order.get("customer_id", ""), {})
    payment = payments_by_order.get(row["order_id"], [])
    payment_type = payment[0]["payment_type"] if payment else "unknown"
    installments = max((int(float(item["payment_installments"] or 0)) for item in payment), default=0)
    on_time = delivered_at is not None and estimated_at is not None and delivered_at <= estimated_at

    order_totals[row["order_id"]]["revenue"] += price
    order_totals[row["order_id"]]["freight"] += freight
    order_totals[row["order_id"]]["units"] += 1

    c = category_stats[category]
    c["orders"].add(row["order_id"])
    c["products"].add(row["product_id"])
    c["sellers"].add(row["seller_id"])
    if order.get("customer_id"):
        c["customers"].add(order["customer_id"])
    c["units"] += 1
    c["revenue"] += price
    c["freight"] += freight
    c["latest_order"] = max(c["latest_order"], order.get("order_purchase_timestamp", ""))
    if review_score:
        c["review_sum"] += review_score
        c["review_count"] += 1
    if status == "delivered":
        c["delivered"] += 1
        c["on_time" if on_time else "late"] += 1
    if status in {"canceled", "unavailable"}:
        c["cancelled"] += 1

    p = product_stats[row["product_id"]]
    p["category"] = category
    p["orders"].add(row["order_id"])
    p["sellers"].add(row["seller_id"])
    p["units"] += 1
    p["revenue"] += price
    p["freight"] += freight
    p["latest_order"] = max(p["latest_order"], order.get("order_purchase_timestamp", ""))
    if review_score:
        p["review_sum"] += review_score
        p["review_count"] += 1
    if status == "delivered":
        p["delivered"] += 1
        p["on_time"] += int(on_time)

    if date:
        d = daily_stats[date]
        d["orders"].add(row["order_id"])
        d["units"] += 1
        d["revenue"] += price
        d["freight"] += freight
        if review_score:
            d["review_sum"] += review_score
            d["review_count"] += 1
        if status == "delivered":
            d["delivered"] += 1
            d["on_time"] += int(on_time)

    if category in fashion_categories:
        order_lines.append({
            "line_id": f"{row['order_id'][:8]}-{int(row['order_item_id']):02d}",
            "order_id": row["order_id"],
            "order_time": order.get("order_purchase_timestamp", ""),
            "order_status": status,
            "product_id": row["product_id"],
            "category": category,
            "seller_id": row["seller_id"],
            "customer_state": customer.get("customer_state", ""),
            "unit_price": f"{price:.2f}",
            "freight_value": f"{freight:.2f}",
            "line_total": f"{price + freight:.2f}",
            "payment_type": payment_type,
            "installments": installments,
            "review_score": f"{review_score:.1f}" if review_score else "",
            "delivered_at": order.get("order_delivered_customer_date", ""),
            "estimated_delivery": order.get("order_estimated_delivery_date", ""),
            "delivery_status": "on_time" if on_time else ("late" if delivered_at else "pending"),
        })

category_rows = []
for category, stats in category_stats.items():
    order_count = len(stats["orders"])
    category_rows.append({
        "category": category,
        "scope": "fashion" if category in fashion_categories else "other",
        "orders": order_count,
        "units": stats["units"],
        "products": len(stats["products"]),
        "sellers": len(stats["sellers"]),
        "customers": len(stats["customers"]),
        "revenue": f"{stats['revenue']:.2f}",
        "avg_item_price": f"{stats['revenue'] / stats['units']:.2f}" if stats["units"] else "0.00",
        "freight_value": f"{stats['freight']:.2f}",
        "freight_ratio": ratio(stats["freight"], stats["revenue"]),
        "avg_review_score": round(ratio(stats["review_sum"], stats["review_count"]), 3),
        "review_count": stats["review_count"],
        "on_time_rate": ratio(stats["on_time"], stats["delivered"]),
        "late_delivery_rate": ratio(stats["late"], stats["delivered"]),
        "cancelled_line_rate": ratio(stats["cancelled"], stats["units"]),
        "latest_order": stats["latest_order"],
    })
category_rows.sort(key=lambda item: float(item["revenue"]), reverse=True)

product_rows = []
for product_id, stats in product_stats.items():
    if stats.get("category") not in fashion_categories:
        continue
    product_rows.append({
        "product_id": product_id,
        "category": stats["category"],
        "orders": len(stats["orders"]),
        "units": stats["units"],
        "sellers": len(stats["sellers"]),
        "revenue": f"{stats['revenue']:.2f}",
        "avg_item_price": f"{stats['revenue'] / stats['units']:.2f}" if stats["units"] else "0.00",
        "freight_ratio": ratio(stats["freight"], stats["revenue"]),
        "avg_review_score": round(ratio(stats["review_sum"], stats["review_count"]), 3),
        "review_count": stats["review_count"],
        "on_time_rate": ratio(stats["on_time"], stats["delivered"]),
        "latest_order": stats["latest_order"],
    })
product_rows.sort(key=lambda item: float(item["revenue"]), reverse=True)

daily_rows = []
for date, stats in sorted(daily_stats.items()):
    daily_rows.append({
        "date": date,
        "orders": len(stats["orders"]),
        "units": stats["units"],
        "revenue": f"{stats['revenue']:.2f}",
        "freight_value": f"{stats['freight']:.2f}",
        "avg_review_score": round(ratio(stats["review_sum"], stats["review_count"]), 3),
        "on_time_rate": ratio(stats["on_time"], stats["delivered"]),
    })

status_counts = Counter(row["order_status"] for row in orders.values())
status_rows = [{"order_status": key, "orders": value, "share": ratio(value, len(orders))} for key, value in status_counts.most_common()]

payment_counts = defaultdict(lambda: {"records": 0, "value": 0.0})
for rows in payments_by_order.values():
    for row in rows:
        item = payment_counts[row["payment_type"]]
        item["records"] += 1
        item["value"] += float(row["payment_value"] or 0)
payment_rows = [
    {"payment_type": key, "records": value["records"], "payment_value": f"{value['value']:.2f}"}
    for key, value in sorted(payment_counts.items(), key=lambda item: item[1]["value"], reverse=True)
]

valid_order_ids = {order_id for order_id, row in orders.items() if row["order_status"] not in {"canceled", "unavailable"}}
total_revenue = sum(order_totals[order_id]["revenue"] for order_id in valid_order_ids)
delivered_orders = [row for row in orders.values() if row["order_status"] == "delivered"]
on_time_orders = sum(
    1 for row in delivered_orders
    if parse_dt(row["order_delivered_customer_date"]) and parse_dt(row["order_estimated_delivery_date"])
    and parse_dt(row["order_delivered_customer_date"]) <= parse_dt(row["order_estimated_delivery_date"])
)
all_reviews = [score for scores in reviews_by_order.values() for score in scores]
summary_rows = [{
    "orders": len(orders),
    "valid_orders": len(valid_order_ids),
    "delivered_orders": len(delivered_orders),
    "cancelled_orders": status_counts["canceled"] + status_counts["unavailable"],
    "cancellation_rate": ratio(status_counts["canceled"] + status_counts["unavailable"], len(orders)),
    "revenue": f"{total_revenue:.2f}",
    "average_order_value": f"{total_revenue / len(valid_order_ids):.2f}",
    "on_time_delivery_rate": ratio(on_time_orders, len(delivered_orders)),
    "average_review_score": round(sum(all_reviews) / len(all_reviews), 3),
    "review_count": len(all_reviews),
    "fashion_order_lines": len(order_lines),
    "fashion_products": len(product_rows),
    "start_date": min(row["order_purchase_timestamp"] for row in orders.values() if row["order_purchase_timestamp"]),
    "end_date": max(row["order_purchase_timestamp"] for row in orders.values() if row["order_purchase_timestamp"]),
}]

order_lines.sort(key=lambda item: item["order_time"], reverse=True)

write_csv("olist_summary.csv", summary_rows, list(summary_rows[0]))
write_csv("olist_category_metrics.csv", category_rows, list(category_rows[0]))
write_csv("olist_product_metrics.csv", product_rows, list(product_rows[0]))
write_csv("olist_daily_metrics.csv", daily_rows, list(daily_rows[0]))
write_csv("olist_order_status_metrics.csv", status_rows, list(status_rows[0]))
write_csv("olist_payment_metrics.csv", payment_rows, list(payment_rows[0]))
write_csv("olist_fashion_order_lines.csv", order_lines, list(order_lines[0]))

print(f"Processed {len(orders):,} orders, {len(order_lines):,} fashion order lines, and {len(product_rows):,} fashion products.")
