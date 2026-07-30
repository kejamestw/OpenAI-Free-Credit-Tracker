import json
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "data" / "models.json"
data = json.loads(path.read_text(encoding="utf-8"))
assert data["schema_version"] == 1
seen = set()
for group in data["groups"].values():
    assert group["daily_quota_tier_1_2"] > 0
    for model in group["models"]:
        assert model["id"] not in seen
        seen.add(model["id"])
        pricing = model["pricing"]
        assert all(pricing[key] >= 0 for key in ("input", "cached_input", "output"))
print(f"models.json valid: {len(seen)} models")
