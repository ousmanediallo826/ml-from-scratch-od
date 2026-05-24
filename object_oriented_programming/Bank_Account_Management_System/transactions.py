"""
Topic 5 — Dataclasses in Python
---------------------------------
@dataclass auto-generates __init__, __repr__, and __eq__ from type annotations.
frozen=True makes instances immutable — perfect for transaction records that
should never change after they're written.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class Transaction:
    """
    Immutable record of a single account event.

    frozen=True means:
      - Every field is read-only after __init__
      - The object is hashable (can live in a set or dict key)
      - Trying to assign tx.amount = 99 raises FrozenInstanceError
    """

    amount:        float
    type:          str        # "deposit" | "withdrawal" | "transfer" | "interest"
    balance_after: float
    timestamp:     str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    note:          str = ""

    def __str__(self):
        sign = "+" if self.amount >= 0 else ""
        return (
            f"[{self.timestamp}]  {self.type:<12} "
            f"{sign}${self.amount:,.2f}  →  balance: ${self.balance_after:,.2f}"
            + (f"  ({self.note})" if self.note else "")
        )