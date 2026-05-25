from portfolio import *
from stock import *

port = Portfolio("Alice", "Alice's Portfolio", risk_level="medium")

port.add_stock(Stock("AAPL", "Apple Inc.",       10, 150.00, 182.50, "Tech")) \
    .add_stock(Stock("TSLA", "Tesla Inc.",        5,  220.00, 185.00, "Auto")) \
    .add_stock(Stock("MSFT", "Microsoft Corp.",   8,  280.00, 340.00, "Tech")) \
    .add_stock(Stock("AMZN", "Amazon.com Inc.",   3,  120.00, 178.00, "Retail")) \
    .add_stock(Stock("META", "Meta Platforms",    6,  300.00, 280.00, "Tech"))

# Magic methods
print(port)                         # __str__
print(len(port))                    # __len__
print("AAPL" in port)              # __contains__
port += Stock("NVDA", "Nvidia",  2, 400.00, 620.00, "Tech")

# Properties
print(port.total_value)             # sum of market values
print(port.total_profit_loss)       # overall P&L
print(port.best_performer)          # highest gain %
print(port.worst_performer)         # biggest loss %
print(port.sectors)                 # {"Tech", "Auto", "Retail"}

# Iterate
for stock in port:                  # __iter__
    print(stock)

# Core methods
port.update_price("TSLA", 195.00)   # update Tesla's price
port.remove_stock("META")           # remove Meta
print(port.find_by_sector("Tech"))  # filter by sector

# ManagedPortfolio extras
print(port.risky_stocks)            # stocks down more than 10%
print(port.rebalance_needed)        # any stock over 40% of portfolio?
port.summary()                      # full breakdown

# Descriptor validation
Stock("BAD", "Bad Corp", -5,  100.00, 120.00)  # raises ValueError
Stock("BAD", "Bad Corp",  5, -100.00, 120.00)  # raises ValueError