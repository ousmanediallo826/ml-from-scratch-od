"""
main.py — PyBank Demo
======================
Exercises every topic:
  2  Class vs Instance Attributes
  3  Properties vs Getters/Setters
  5  Dataclasses
  7  Magic Methods
  9  Descriptors
  10 Inheritance
"""

from account  import Account
from accounts import SavingsAccount, CheckingAccount, BusinessAccount


def section(title):
    print(f"\n{'═'*60}\n  {title}\n{'═'*60}")


# ── Topic 2 — Class vs Instance Attributes ───────────────────────────
section("TOPIC 2 — Class vs Instance Attributes")

alice = SavingsAccount("Alice",  initial_deposit=5_000, interest_rate=0.04)
bob   = CheckingAccount("Bob",   initial_deposit=1_200, overdraft_limit=500)
corp  = BusinessAccount("Carol", business_name="TechCo", initial_deposit=20_000)

print(f"\nClass attr   →  Account.bank_name     : {Account.bank_name!r}")
print(f"Class attr   →  Account.total_accounts: {Account.total_accounts}")
print(f"Instance attr →  alice.account_number : {alice.account_number!r}")
print(f"Instance attr →  bob.account_number   : {bob.account_number!r}")

print(f"\nShadowing the class attr on ONE instance:")
alice.bank_name = "AliceBank"
print(f"  alice.bank_name → {alice.bank_name!r}  (instance shadow)")
print(f"  bob.bank_name   → {bob.bank_name!r}  (still from class)")
alice.bank_name = "PyBank"


# ── Topic 3 — Properties vs Getters and Setters ──────────────────────
section("TOPIC 3 — Properties vs Getters and Setters")

print(f"\n@property (reads like an attribute):")
print(f"  alice.transaction_count → {alice.transaction_count}")
print(f"  bool(corp)              → {bool(corp)}")

print(f"\nTraditional getter/setter (explicit method calls):")
print(f"  alice.get_owner()       → {alice.get_owner()!r}")
alice.set_owner("Alice Smith")
print(f"  after set_owner(...)    → {alice.owner!r}")
alice.set_owner("Alice")


# ── Topic 5 — Dataclasses ────────────────────────────────────────────
section("TOPIC 5 — Dataclasses (Transaction)")

alice.deposit(1_000, "salary").deposit(200, "freelance").withdraw(150, "groceries")

print("\nTransaction objects (frozen=True — immutable):")
for tx in alice._transactions:
    print(f"  {tx}")

print(f"\nTrying to mutate a frozen dataclass:")
try:
    alice._transactions[0].amount = 9999
except Exception as e:
    print(f"  ✗  {type(e).__name__}: {e}")


# ── Topic 7 — Magic Methods ──────────────────────────────────────────
section("TOPIC 7 — Magic Methods")

print(f"\n__str__      → {alice}")
print(f"__repr__     → {repr(alice)}")
print(f"__len__      → len(alice) = {len(alice)}")
print(f"__bool__     → bool(alice) = {bool(alice)}")
print(f"__contains__ → 1000 in alice = {1000 in alice}")
print(f"__contains__ → 9999 in alice = {9999 in alice}")

print(f"\n__lt__ / sorted():")
dave = SavingsAccount("Dave", initial_deposit=800)
eve  = CheckingAccount("Eve",  initial_deposit=3_200)
for acc in sorted([alice, bob, corp, dave, eve]):
    print(f"  {acc.owner:<10} ${acc.balance:>10,.2f}")

print(f"\n__add__ — alice + dave:")
print(f"  {alice + dave}")


# ── Topic 9 — Descriptors ────────────────────────────────────────────
section("TOPIC 9 — Descriptors")

print("\nPositiveNumber blocks negative values:")
try:
    alice.balance = -500
except ValueError as e:
    print(f"  ✗  {e}")

print("\nPositiveNumber blocks wrong types:")
try:
    alice.balance = "lots of money"
except TypeError as e:
    print(f"  ✗  {e}")

print("\nBoundedRate blocks out-of-range rates:")
try:
    alice.interest_rate = 1.5
except ValueError as e:
    print(f"  ✗  {e}")

print(f"\nAccessing descriptor on the class itself:")
print(f"  Account.balance → {Account.balance!r}")


# ── Topic 10 — Inheritance ───────────────────────────────────────────
section("TOPIC 10 — Inheritance")

print("\nMRO for BusinessAccount:")
for cls in BusinessAccount.__mro__:
    print(f"  {cls}")

print(f"\nSavingsAccount.apply_interest():")
before = alice.balance
earned = alice.apply_interest()
print(f"  Before: ${before:,.2f}  |  Earned: ${earned:,.2f}  |  After: ${alice.balance:,.2f}")

print(f"\nCheckingAccount overdraft:")
print(f"  Bob balance: ${bob.balance:,.2f}, overdraft: ${bob.overdraft_limit:,.2f}")
bob.withdraw(1_600, "rent")
print(f"  After $1,600 withdrawal: ${bob.balance:,.2f}")
try:
    bob.withdraw(500)
except ValueError as e:
    print(f"  ✗  Blocked: {e}")

print(f"\nBusinessAccount credit line:")
print(f"  Available: ${corp.credit_available:,.2f}")
corp.request_loan(4_000, "equipment")
print(f"  After $4,000 draw: ${corp.credit_available:,.2f} left")
corp.repay_loan(1_500)
print(f"  After $1,500 repay: ${corp.credit_available:,.2f} left")

print(f"\nFull statement — Alice:")
print(alice.statement)

section("ALL TOPICS DEMONSTRATED SUCCESSFULLY ✓")