def fetch_costs(client, start_time: int) -> dict:
    try:
        payload = client.get("/organization/costs", {"start_time": start_time, "bucket_width": "1d", "limit": 1})
        total = sum(
            float((row.get("amount") or {}).get("value") or 0)
            for bucket in payload.get("data", [])
            for row in bucket.get("results", [])
        )
        return {"actual": total, "error": None}
    except Exception as exc:
        return {"actual": 0.0, "error": str(exc)}
