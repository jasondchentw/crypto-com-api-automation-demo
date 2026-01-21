# Crypto.com Exchange Market Data Automation Demo ⭐

**Senior QA Engineer 級別作品** | Python + Behave + Domain-Driven BDD | 完整自動化 Crypto.com 公開市場資料 API

涵蓋：
- REST: `public/get-candlestick`
- WebSocket: `book.{instrument_name}.{depth}`

## 設計理念（簡短說明）

採用**領域導向行為驅動測試（Domain-Oriented BDD）**：
- Gherkin 使用交易員業務語言（非技術語言）
- 領域層（domain）定義 Candlestick / OrderBook 物件，提供語意化驗證
- 技術細節封裝於 infrastructure 層（連線、重試、格式處理）
- 業務邏輯集中在 domain/services，便於擴充其他端點（如 ticker、trade）

**測試案例重點**：
- REST：正常取得 K 線、無效幣種錯誤、結構完整性、數量近似
- WebSocket：初始快照、持續增量更新、深度限制、價格精度（Decimal 防浮點誤差）

本專案使用**真實市場即時資料**測試，無 mock，貼近生產環境。

## 快速開始（Setup Guide）

```bash
# 1. Clone 專案
git clone https://github.com/[你的帳號]/crypto-com-market-bdd-demo.git
cd crypto-com-market-bdd-demo

# 2. 安裝依賴
pip install -r requirements.txt

# 3. 執行測試
behave                                # 全部
behave features/01_candlestick.feature # 只測 REST
behave features/02_orderbook.feature   # 只測 WebSocket

# 4. 產生 Allure 美觀報告（推薦）
behave -f allure_behave.formatter:AllureFormatter -o reports/
allure serve reports/
