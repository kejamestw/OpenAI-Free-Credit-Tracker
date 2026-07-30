# OpenAI Free Credit Tracker

> 本機優先的 OpenAI 每日免費 Token 額度、適用模型、Service Tier 與 API 成本監控工具。

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB)
![License](https://img.shields.io/badge/License-Apache--2.0-green)
![Status](https://img.shields.io/badge/status-alpha-orange)

[English](README.en.md) | 繁體中文

## 功能

- 分別追蹤高階模型群組與 Mini／Nano 群組的每日免費 Token。
- 主圖只計入 OpenAI Usage API 明確標示為 `incentivized-tier` 或 data-sharing incentive 的流量。
- 每日以 `00:00 UTC` 重置，介面同時顯示台灣時間區間。
- 模型名稱自動移除快照日期。
- 模型膠囊顯示費用高／中／低標籤，滑鼠移入可查看價格與計算公式。
- Usage API 與 Costs API 分開處理，成本查詢失敗不會阻擋額度顯示。
- Admin API Key 僅保留在程式記憶體，不寫入磁碟或瀏覽器儲存空間。
- 本機服務只監聽 `127.0.0.1`。

## 重要聲明

本專案是非官方工具，與 OpenAI 無隸屬或背書關係。免費額度、適用模型與價格可能變動，請以 OpenAI 官方文件及帳務後台為準。

請勿將 Admin API Key 貼到第三方網站、公開 Issue、截圖或 Git Commit 中。

## 快速開始

### Windows

1. 安裝 Python 3.10 或以上版本。
2. 下載 Repository，或執行 `git clone`。
3. 雙擊 `scripts/run_windows.bat`。
4. 瀏覽器開啟後，貼入以 `sk-admin-` 開頭且可讀取 Usage 的 Admin API Key。
5. 按下「更新今日資料」。

### 命令列

```bash
python -m quota_monitor
```

如果尚未安裝本專案：

```bash
python -m pip install -e .
python -m quota_monitor
```

## 建立 Windows EXE

```bat
scriptsuild_windows.bat
```

完成後檔案位於：

```text
dist\OpenAI-Free-Credit-Tracker.exe
```

## 專案結構

```text
src/quota_monitor/   Python 後端與 OpenAI API 邏輯
web/                 HTML、CSS、JavaScript
data/models.json     模型群組、別名與價格
tests/               單元測試與匿名 Fixture
docs/                架構、安全與價格文件
.github/              CI、Issue 與 PR 模板
```

## 費用標籤

費用級距以「1,000 Input Token + 1,000 Output Token」的標準案例判斷：

- 低：低於 US$0.003
- 中：US$0.003 至未滿 US$0.012
- 高：US$0.012 以上

公式：

```text
成本 =
  非快取輸入 Token × Input 單價 / 1,000,000
+ 快取輸入 Token × Cached Input 單價 / 1,000,000
+ 輸出 Token × Output 單價 / 1,000,000
```

## 已知限制

- Usage 與 Costs 資料可能延遲。
- 剩餘免費額度是依 API 的 Service Tier 標記推算，不是官方餘額保證。
- 成本標籤是快速比較，不代表模型品質。
- 目前集中於 Completions Usage，工具、微調與 Evals 不在主要統計範圍。

## 貢獻

歡迎回報錯誤、更新價格、改善 UI 或增加測試。請先閱讀 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 安全性

請勿在公開 Issue 貼出金鑰或完整敏感 JSON。請閱讀 [SECURITY.md](SECURITY.md)。

## 授權

Apache License 2.0。詳見 [LICENSE](LICENSE)。
