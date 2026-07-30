import json
from pathlib import Path
from quota_monitor.model_catalog import load_catalog
from quota_monitor.usage_service import summarize_usage


def test_only_incentivized_usage_enters_main_cards():
    fixture = json.loads((Path(__file__).parent / "fixtures" / "usage_incentivized.json").read_text())
    result = summarize_usage(fixture, load_catalog())
    assert result["groups"]["mini"]["total"] == 1100
    assert result["other_tokens"] == 0
