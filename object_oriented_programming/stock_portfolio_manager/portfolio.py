from stock import Stock


class Portfolio:
    currency = "USD"

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.stocks = []

    @property
    def total_value(self):
        return sum(stock.current_price * stock.shares for stock in self.stocks)

    @property
    def total_invested(self):
        return sum(stock.buy_price * stock.shares for stock in self.stocks)

    @property
    def total_profit_loss(self):
        return self.total_value - self.total_invested

    @property
    def best_performer(self):
        if not self.stocks:
            return None
        return max(self.stocks, key=lambda stock: stock.profit_loss_percent)

    @property
    def worst_performer(self):
        if not self.stocks:
            return None
        return min(self.stocks, key=lambda stock: stock.profit_loss_percent)

    @property
    def sectors(self):
        return {stock.sector for stock in self.stocks}

    def add_stock(self, stock: str):
        self.stocks.append(stock)
        return self

    def remove_stock(self, stock: str):
        if stock not in self.stocks:
            raise ValueError(f"Stock {stock} not in portfolio")
        self.stocks.remove(stock)

    def filter_by_sector(self, sector: str):
        return [stock for stock in self.stocks if stock.sector == sector]

    def update_price(self, ticker: str, new_price: float):
        for stock in self.stocks:
            if stock.ticker == ticker:
                stock.current_price = new_price
                return stock

        raise ValueError(f"Stock {ticker} not in portfolio")

    def __str__(self):
        return f"{self.currency} | {self.owner}'s {self.name} Portfolio | {len(self.stocks)} stocks | value: ${self.total_value:.2f}"

    def __len__(self):
        return len(self.stocks)

    def __contains__(self, stock: Stock):
        return stock in self.stocks

    def __iter__(self):
        return iter(self.stocks)