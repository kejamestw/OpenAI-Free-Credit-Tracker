# OpenAI Free Credit Tracker

A local-first dashboard for monitoring OpenAI complimentary daily tokens, eligible models, service tiers, and estimated API costs.

## Highlights

- Tracks complimentary traffic in separate model groups.
- Counts only usage explicitly marked as incentivized or data-sharing traffic in the main quota cards.
- Keeps the Admin API key in memory only.
- Binds the local server to `127.0.0.1`.
- Shows model pricing tooltips and transparent low/medium/high cost tags.

## Run

```bash
python -m pip install -e .
python -m quota_monitor
```

On Windows, you may double-click `scripts/run_windows.bat`.

## Disclaimer

This is an unofficial community project and is not affiliated with or endorsed by OpenAI. Pricing, model eligibility, and complimentary-token rules may change.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md) before opening a pull request or security report.
