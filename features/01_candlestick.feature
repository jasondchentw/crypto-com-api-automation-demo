Feature: 交易員取得歷史 K 線資料分析市場趨勢

  Scenario Outline: 成功取得主流交易對 K 線
    Given 交易員關注交易對 "<instrument>"
    And 選擇時間粒度 "<timeframe>"
    When 請求最近 <count> 根 K 線
    Then 應收到正確的 "<instrument>" K 線資料
    And K 線數量接近 <count> 根
    And 每根 K 棒包含開高低收與成交量

    Examples:
      | instrument   | timeframe | count |
      | BTC_USD      | 5m        | 200   |
      | ETH_USDT     | 1h        | 100   |

  Scenario: 查詢無效交易對
    Given 交易員輸入無效交易對 "FAKE999"
    When 請求 K 線資料
    Then 系統應回傳錯誤訊息