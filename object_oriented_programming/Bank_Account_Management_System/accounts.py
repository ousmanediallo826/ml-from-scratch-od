"""
Topic 10 — Inheritance
------------------------
Three subclasses all extend Account.  Each one:
  - calls super().__init__() to reuse the parent constructor
  - adds its own class and instance attributes
  - overrides or extends core methods (deposit, withdraw)
  - inherits magic methods, descriptors, and properties for free
"""

from account     import Account
from descriptors import BoundedRate, PositiveNumber


# ── SavingsAccount ────────────────────────────────────────────────────

class SavingsAccount(Account):
    """Earns interest. Single deposits are capped at $50,000."""

    default_rate: float = 0.03   # class attribute — shared default

    interest_rate = BoundedRate()  # descriptor on the subclass

    def __init__(self, owner: str, initial_deposit: float = 0.0,
                 interest_rate: float = None):
        super().__init__(owner, initial_deposit)
        self.interest_rate = interest_rate or SavingsAccount.default_rate
        self._account_type = "Savings"

    def deposit(self, amount: float, note: str = "") -> "SavingsAccount":
        if amount > 50_000:
            raise ValueError("Single deposit cannot exceed $50,000 for savings accounts.")
        return super().deposit(amount, note)

    def apply_interest(self) -> float:
        """Credit one period of interest to the account."""
        earned = round(self.balance * self.interest_rate, 2)
        self.balance += earned
        self._record(earned, "interest", f"Rate: {self.interest_rate*100:.2f}%")
        return earned

    def __str__(self) -> str:
        return f"{super().__str__()} [Savings @ {self.interest_rate*100:.1f}%]"


# ── CheckingAccount ───────────────────────────────────────────────────

class CheckingAccount(Account):
    """Everyday spending account with an optional overdraft buffer."""

    default_overdraft: float = 0.0

    overdraft_limit = PositiveNumber()

    def __init__(self, owner: str, initial_deposit: float = 0.0,
                 overdraft_limit: float = None):
        super().__init__(owner, initial_deposit)
        self.overdraft_limit = overdraft_limit or CheckingAccount.default_overdraft
        self._account_type = "Checking"

    def withdraw(self, amount: float, note: str = "") -> "CheckingAccount":
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        available = self.balance + self.overdraft_limit
        if amount > available:
            raise ValueError(
                f"Exceeds available funds including overdraft. "
                f"Available: ${available:,.2f}"
            )
        # Write directly to _balance to bypass the descriptor's
        # non-negative guard — overdraft accounts can go negative intentionally
        self._balance = round(self.balance - amount, 2)
        self._record(-amount, "withdrawal", note)
        return self

    def __str__(self) -> str:
        return f"{super().__str__()} [Checking | overdraft: ${self.overdraft_limit:,.2f}]"


# ── BusinessAccount ───────────────────────────────────────────────────

class BusinessAccount(Account):
    """Corporate account with a credit line and loan management."""

    default_credit_limit: float = 10_000.0

    credit_limit = PositiveNumber()

    def __init__(self, owner: str, business_name: str,
                 initial_deposit: float = 0.0,
                 credit_limit: float = None):
        super().__init__(owner, initial_deposit)
        self.business_name = business_name
        self.credit_limit  = credit_limit or BusinessAccount.default_credit_limit
        self.credit_used   = 0.0
        self._account_type = "Business"

    @property
    def credit_available(self) -> float:
        """Read-only: remaining credit line."""
        return round(self.credit_limit - self.credit_used, 2)

    def request_loan(self, amount: float, note: str = "") -> float:
        """Draw against the credit line."""
        if amount <= 0:
            raise ValueError("Loan amount must be positive.")
        if amount > self.credit_available:
            raise ValueError(
                f"Amount exceeds available credit. Available: ${self.credit_available:,.2f}"
            )
        self.credit_used += amount
        self.balance     += amount
        self._record(amount, "loan", note or f"Credit draw — {self.business_name}")
        return self.credit_available

    def repay_loan(self, amount: float) -> float:
        """Pay back part of the credit line."""
        repay = min(amount, self.credit_used)
        self.balance     -= repay
        self.credit_used -= repay
        self._record(-repay, "loan repay", "Credit repayment")
        return self.credit_available

    def __str__(self) -> str:
        return (
            f"{super().__str__()} "
            f"[{self.business_name} | credit: ${self.credit_available:,.2f} avail]"
        )