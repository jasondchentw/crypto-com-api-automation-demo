Feature: 交易員即時監控市場深度買賣盤

  Scenario Outline: 成功訂閱並接收買賣盤更新
    When 訂閱 "<instrument>" 深度 <depth> 買賣盤
    Then 先收到完整初始快照
    And 持續收到至少 5 次增量更新
    And 深度不超過 <depth>

    Examples:
      | instrument   | depth |
      | BTC_USD      | 10    |
      | ETH_USDT     | 50    |