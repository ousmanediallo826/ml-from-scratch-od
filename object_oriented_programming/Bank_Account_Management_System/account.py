"""
Topics covered in this file
----------------------------
  2  — Class vs Instance Attributes
  3  — Properties vs Getters & Setters
  7  — Magic Methods
  9  — Descriptors (via imported descriptor classes)
"""

from descriptors  import PositiveNumber
from transactions import Transaction


class Account:
    """
    Base class for all account types.

    CLASS ATTRIBUTES (Topic 2)
      Shared by every Account instance and every subclass.

    DESCRIPTORS (Topic 9)
      `balance` is a PositiveNumber descriptor — validation is handled
      by the class itself, not scattered across every method.
    """

    # ── Class attributes ──────────────────────────────────────────────
    bank_name:        str = "PyBank"   # same for every account
    total_accounts:   int = 0          # increments with every new account
    _account_counter: int = 1000       # used to auto-generate account numbers

    # Descriptor — lives on the class, guards ALL instances
    balance = PositiveNumber()

    # ── Constructor ───────────────────────────────────────────────────
    def __init__(self, owner: str, initial_deposit: float = 0.0):
        """
        Instance attributes are unique to each object.
        owner, account_number, _transactions differ per instance;
        bank_name and total_accounts are shared across all.
        """
        self.owner  = owner
        self.balance = initial_deposit        # goes through the descriptor

        Account._account_counter += 1
        self.account_number = f"ACC-{Account._account_counter}"
        self._transactions: list[Transaction] = []

        Account.total_accounts += 1

        if initial_deposit > 0:
            self._record(initial_deposit, "deposit", "Account opened")

    # ── Properties (Topic 3) ──────────────────────────────────────────
    # Clean public API — reads like a normal attribute but runs code.

    @property
    def transaction_count(self) -> int:
        """Read-only: how many transactions have been recorded."""
        return len(self._transactions)

    @property
    def statement(self) -> str:
        """Read-only: formatted mini-statement."""
        lines = [
            f"{'─'*55}",
            f"  {self.bank_name}  |  {self.account_number}  |  {self.owner}",
            f"{'─'*55}",
        ]
        if not self._transactions:
            lines.append("  No transactions yet.")
        else:
            for tx in self._transactions:
                lines.append(f"  {tx}")
        lines += [
            f"{'─'*55}",
            f"  Current balance:  ${self.balance:,.2f}",
            f"{'─'*55}",
        ]
        return "\n".join(lines)

    # Traditional getter/setter pair (Topic 3 contrast)
    # These work identically to a property but require explicit method calls.
    # account.get_owner() vs just account.owner — properties win every time.
    def get_owner(self) -> str:
        return self.owner

    def set_owner(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Owner name must be a non-empty string.")
        self.owner = name.strip()

    # ── Core methods ──────────────────────────────────────────────────
    def deposit(self, amount: float, note: str = "") -> "Account":
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self._record(amount, "deposit", note)
        return self   # enables chaining: acc.deposit(100).deposit(50)

    def withdraw(self, amount: float, note: str = "") -> "Account":
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError(
                f"Insufficient funds. Balance: ${self.balance:,.2f}, "
                f"requested: ${amount:,.2f}"
            )
        self.balance -= amount
        self._record(-amount, "withdrawal", note)
        return self

    def _record(self, amount: float, type_: str, note: str = ""):
        """Append an immutable Transaction dataclass to the history."""
        self._transactions.append(
            Transaction(amount=amount, type=type_,
                        balance_after=self.balance, note=note)
        )

    # ── Magic Methods (Topic 7) ───────────────────────────────────────

    def __str__(self) -> str:
        """Human-readable: used by print()."""
        return (
            f"{self.bank_name} | {self.account_number} | "
            f"{self.owner} | ${self.balance:,.2f}"
        )

    def __repr__(self) -> str:
        """Developer-facing: used in the REPL and for debugging."""
        return (
            f"{type(self).__name__}("
            f"owner={self.owner!r}, "
            f"account_number={self.account_number!r}, "
            f"balance={self.balance!r})"
        )

    def __add__(self, other: "Account") -> "Account":
        """Merge two accounts: account_a + account_b creates a new one."""
        if not isinstance(other, Account):
            return NotImplemented
        merged = Account(
            owner           = f"{self.owner} & {other.owner}",
            initial_deposit = self.balance + other.balance,
        )
        return merged

    def __lt__(self, other: "Account") -> bool:
        """Enables sorting: sorted(accounts) orders by balance ascending."""
        if not isinstance(other, Account):
            return NotImplemented
        return self.balance < other.balance

    def __eq__(self, other: object) -> bool:
        """Two accounts are equal if they share the same account number."""
        if not isinstance(other, Account):
            return NotImplemented
        return self.account_number == other.account_number

    def __len__(self) -> int:
        """len(account) returns the transaction count."""
        return self.transaction_count

    def __contains__(self, amount: float) -> bool:
        """500 in account → True if any transaction had that exact amount."""
        return any(abs(tx.amount) == amount for tx in self._transactions)

    def __bool__(self) -> bool:
        """An account is truthy if it has a positive balance."""
        return getattr(self, "_balance", 0) > 0