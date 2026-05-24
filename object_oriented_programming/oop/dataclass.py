from dataclasses import dataclass, field
from datetime import datetime
@dataclass
class Transaction:
    amount: float
    type: str
    note: str = ""
    timestamp: str  = field( default_factory=lambda: datetime.now().strftime("%H:%M") )



tx = Transaction(100.0, "deposit", "salary")
print(tx)
print(tx.amount)
print(tx.timestamp)


