# Architecture

瀏覽器只與 `127.0.0.1` 的 Python Server 通訊。Admin Key 透過自訂 Header 傳給本機 Server，再由 Server 呼叫 OpenAI Admin Usage API。Key 不會寫入網址、磁碟或 localStorage。

核心資料流：

```text
Browser UI -> Local Python Server -> OpenAI Admin API
           <- Aggregated JSON      <- Usage / Costs
```
