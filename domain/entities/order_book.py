from decimal import Decimal
from typing import List, Tuple

class OrderBook:
    def __init__(self, bids: List[Tuple[str, str]], asks: List[Tuple[str, str]]):
        self.bids = [(Decimal(p), Decimal(q)) for p, q in bids]
        self.asks = [(Decimal(p), Decimal(q)) for p, q in asks]

    def depth(self) -> int:
        return max(len(self.bids), len(self.asks))

    def is_valid(self) -> bool:
        return all(q > 0 for _, q in self.bids + self.asks)