from behave import fixture
from infrastructure.rest_client import RestClient
from infrastructure.websocket_manager import WebSocketManager

def before_all(context):
    context.rest_client = RestClient("https://api.crypto.com/exchange/v1")
    context.ws_manager = WebSocketManager("wss://stream.crypto.com/exchange/v1/market")

def after_scenario(context, scenario):
    if hasattr(context, 'ws_manager'):
        context.ws_manager.close()