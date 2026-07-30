def is_incentivized(service_tier: str | None) -> bool:
    value = (service_tier or "").lower()
    return "incentiv" in value or "data_sharing" in value


def estimate_cost(input_tokens: int, cached_tokens: int, output_tokens: int, pricing: dict) -> float:
    uncached = max(0, input_tokens - cached_tokens)
    return (
        uncached * pricing["input"]
        + cached_tokens * pricing["cached_input"]
        + output_tokens * pricing["output"]
    ) / 1_000_000


def cost_level(pricing: dict, low_below: float = 0.003, high_from: float = 0.012) -> str:
    sample_cost = (1000 * pricing["input"] + 1000 * pricing["output"]) / 1_000_000
    if sample_cost >= high_from:
        return "high"
    if sample_cost >= low_below:
        return "medium"
    return "low"
