# Security notes

- Server 必須只綁定 `127.0.0.1`。
- 不得將 Admin Key 放入 URL、Log、localStorage 或 Repository。
- 測試 Fixture 必須匿名且不得含真實 Project ID。
- 發布 EXE 前應掃描 Repository 歷史是否含任何 `sk-admin-` 或 `sk-proj-` 字串。
