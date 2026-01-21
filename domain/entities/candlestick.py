from decimal import Decimal

class Candlestick:
    def __init__(self, t: int, o: str, h: str, l: str, c: str, v: str):
        self.timestamp = t
        self.open = Decimal(o)
        self.high = Decimal(h)
        self.low = Decimal(l)
        self.close = Decimal(c)
        self.volume = Decimal(v)

    def is_valid(self) -> bool:
        return self.high >= self.low and self.volume >= 0