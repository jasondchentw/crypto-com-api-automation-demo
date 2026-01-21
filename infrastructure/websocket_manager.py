import websocket
import json
import threading
from typing import List, Callable

class WebSocketManager:
    def __init__(self, ws_url: str):
        self.ws_url = ws_url
        self.ws = None
        self.on_update_callback: Callable = None
        self.updates = []
        self._connect()

    def _connect(self):
        self.ws = websocket.WebSocketApp(
            self.ws_url,
            on_open=self._on_open,
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close
        )
        self.thread = threading.Thread(target=self.ws.run_forever, daemon=True)
        self.thread.start()

    def _on_open(self, ws):
        print("WebSocket connected")

    def _on_message(self, ws, message):
        try:
            data = json.loads(message)
            if "result" in data and data.get("method") == "subscribe":
                print("Subscription confirmed")
            elif "result" in data and "data" in data["result"]:
                # 簡化處理 order book 更新
                book = data["result"]["data"][0]
                if self.on_update_callback:
                    self.on_update_callback(book)
                self.updates.append(book)
        except Exception as e:
            print(f"Message parse error: {e}")

    def _on_error(self, ws, error):
        print(f"WS error: {error}")

    def _on_close(self, ws, code, reason):
        print("WebSocket closed")

    def subscribe(self, channels: List[str]):
        if not self.ws:
            return
        payload = {
            "method": "subscribe",
            "params": {"channels": channels},
            "id": 987654
        }
        self.ws.send(json.dumps(payload))

    def set_update_callback(self, callback: Callable):
        self.on_update_callback = callback

    def close(self):
        if self.ws:
            self.ws.close()