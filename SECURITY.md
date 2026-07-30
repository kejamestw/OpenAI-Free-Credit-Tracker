# Security Policy

## Supported versions

目前只支援最新的 alpha 版本。

## Reporting a vulnerability

請不要在公開 Issue 貼出漏洞細節、Admin API Key、Project Key 或敏感 API 回應。

在 GitHub Repository 的 **Security** 頁面使用 **Report a vulnerability** 私下通報。若該功能尚未啟用，請先建立不含敏感細節的 Issue，要求維護者提供私下聯絡方式。

## Security design

- 本機 HTTP Server 只綁定 `127.0.0.1`。
- Admin API Key 預設只存在記憶體。
- 不使用 URL Query String 傳遞金鑰。
- 不將金鑰寫入 localStorage、設定檔或 Log。
