from behave import when, then
from infrastructure.websocket_manager import WebSocketManager

@when('訂閱 "{instrument}" 深度 {depth:d} 買賣盤')
def step_subscribe_orderbook(context, instrument, depth):
    channel = f"book.{instrument}.{depth}"
    context.ws_manager.subscribe([channel])
    context.orderbook_updates = []

    def callback(update):
        context.orderbook_updates.append(update)

    context.ws_manager.set_update_callback(callback)

@then('先收到完整初始快照')
def step_check_snapshot(context):
    # 等待一段時間收集資料
    import time
    time.sleep(6)
    assert len(context.orderbook_updates) > 0

@then('持續收到至少 5 次增量更新')
def step_check_updates(context):
    assert len(context.orderbook_updates) >= 5

@then('深度不超過 {max_depth:d}')
def step_check_depth(context, max_depth):
    for update in context.orderbook_updates:
        bids_len = len(update.get('bids', []))
        asks_len = len(update.get('asks', []))
        assert max(bids_len, asks_len) <= max_depth