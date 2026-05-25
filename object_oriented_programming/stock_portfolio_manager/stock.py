from dataclasses import dataclass
from descriptors import ShareCount, PositivePrice


@dataclass
class Stock:
    ticker: str
    company: str
    shares: int
    buy_price: float
    current_price: float
    sector: str = "Unknown"

    shares = ShareCount()
    buy_price = PositivePrice()
    current_price = PositivePrice()

    def __post_init__(self):
        self.shares = self.shares
        self.buy_price = self.buy_price
        self.current_price = self.current_price

    @property
    def profit_loss(self):
        return (self.current_price - self.buy_price) * self.shares

    @property
    def profit_loss_percent(self):
        return ((self.current_price - self.buy_price) / self.buy_price) * 100

    @property
    def is_profitable(self):
        return self.current_price > self.buy_price

    @property
    def market_value(self):
        return self.current_price * self.shares

    def __str__(self):
        return (
            f"{self.ticker} | {self.company} | "
            f"{self.shares} shares @ ${self.buy_price:.2f} | "
            f"Current: ${self.current_price:.2f} | "
            f"Value: ${self.market_value:.2f} | "
            f"P&L: ${self.profit_loss:.2f} "
            f"({self.profit_loss_percent:.2f}%)"
        )