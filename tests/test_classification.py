from quota_monitor.classification import cost_level, estimate_cost, is_incentivized


def test_incentivized_tier():
    assert is_incentivized("incentivized-tier")
    assert not is_incentivized("default")


def test_cost_calculation_does_not_double_count_cached_tokens():
    pricing = {"input": 2.5, "cached_input": 0.25, "output": 15}
    value = estimate_cost(1000, 400, 100, pricing)
    expected = (600 * 2.5 + 400 * 0.25 + 100 * 15) / 1_000_000
    assert value == expected


def test_cost_level():
    assert cost_level({"input": 0.2, "output": 1.25}) == "low"
    assert cost_level({"input": 0.75, "output": 4.5}) == "medium"
    assert cost_level({"input": 5, "output": 30}) == "high"
