from behave import given, when, then
from infrastructure.rest_client import RestClient
from domain.entities.candlestick import Candlestick

@given('交易員關注交易對 "{instrument}"')
def step_set_instrument(context, instrument):
    context.instrument = instrument

@given('選擇時間粒度 "{timeframe}"')
def step_set_timeframe(context, timeframe):
    context.timeframe = timeframe

@when('請求最近 {count:d} 根 K 線')
def step_request_candles(context, count):
    client = context.rest_client
    params = {
        "instrument_name": context.instrument,
        "timeframe": context.timeframe,
        "depth": count   # 注意：文件用 depth 而非 count
    }
    context.response = client.public_post("get-candlestick", params)
    context.candles = [
        Candlestick(d['t'], d['o'], d['h'], d['l'], d['c'], d['v'])
        for d in context.response.get('result', {}).get('data', [])
    ]

@then('應收到正確的 "{instrument}" K 線資料')
def step_verify_instrument(context, instrument):
    assert context.response.get('result', {}).get('instrument_name') == instrument

@then('K 線數量接近 {count:d} 根')
def step_check_count(context, count):
    actual = len(context.candles)
    assert abs(actual - count) <= 20, f"Expected ~{count}, got {actual}"

@then('每根 K 棒包含開高低收與成交量')
def step_check_fields(context):
    assert all(c.is_valid() for c in context.candles)