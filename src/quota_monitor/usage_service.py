from datetime import datetime, timezone

from .classification import estimate_cost, is_incentivized
from .model_catalog import clean_model_name, find_model


def utc_day_range(now: datetime | None = None) -> tuple[int, int]:
    current = now or datetime.now(timezone.utc)
    start = current.astimezone(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    return int(start.timestamp()), int(current.timestamp())


def fetch_usage(client, catalog: dict, now: datetime | None = None) -> dict:
    start, end = utc_day_range(now)
    params = {
        "start_time": start,
        "end_time": end,
        "bucket_width": "1h",
        "limit": 24,
        "group_by": ["model", "project_id", "service_tier"],
    }
    buckets = []
    page = None
    while True:
        if page:
            params["page"] = page
        payload = client.get("/organization/usage/completions", params)
        buckets.extend(payload.get("data", []))
        page = payload.get("next_page")
        if not page:
            break
    return summarize_usage(buckets, catalog, start, end)


def summarize_usage(buckets: list, catalog: dict, start: int = 0, end: int = 0) -> dict:
    groups = {
        group_id: {"input": 0, "output": 0, "total": 0, "models": {}}
        for group_id in catalog["groups"]
    }
    other_tokens = 0
    list_price = 0.0
    debug = []
    for bucket in buckets:
        for row in bucket.get("results", []):
            raw_name = row.get("model") or "unknown"
            display_name = clean_model_name(raw_name)
            entry = find_model(raw_name, catalog)
            input_tokens = int(row.get("input_tokens") or 0)
            cached_tokens = int(row.get("input_cached_tokens") or 0)
            output_tokens = int(row.get("output_tokens") or 0)
            total = input_tokens + output_tokens
            free = is_incentivized(row.get("service_tier"))
            if entry:
                list_price += estimate_cost(input_tokens, cached_tokens, output_tokens, entry["pricing"])
            if free and entry:
                group = groups[entry["group"]]
                group["input"] += input_tokens
                group["output"] += output_tokens
                group["total"] += total
                model = group["models"].setdefault(display_name, {"input": 0, "output": 0, "total": 0})
                model["input"] += input_tokens
                model["output"] += output_tokens
                model["total"] += total
            else:
                other_tokens += total
            debug.append({"model": display_name, "service_tier": row.get("service_tier"), "tokens": total})
    return {"groups": groups, "other_tokens": other_tokens, "list_price": list_price, "start": start, "end": end, "debug": debug}
