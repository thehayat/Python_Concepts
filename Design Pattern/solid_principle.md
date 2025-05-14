🅢 — Single Responsibility Principle (SRP)
One class = One job

A class should have only one reason to change, meaning it should do just one thing.

✅ Example:
A ReportPrinter class should only handle printing, not generating reports.
```python
# BAD: One class doing too much
class Report:
    def generate(self):
        return "Report Data"

    def print_report(self):
        print(self.generate())

# GOOD: Split responsibilities
class Report:
    def generate(self):
        return "Report Data"

class ReportPrinter:
    def print(self, report: Report):
        print(report.generate())
```



🅞 — Open/Closed Principle (OCP)
Open for extension, closed for modification

You should be able to add new behavior without changing existing code.

✅ Example:
Use inheritance or interfaces to extend functionality, rather than modifying core logic.

```python
# GOOD: Add new behavior via inheritance
class Discount:
    def calculate(self, price):
        return price

class SeasonalDiscount(Discount):
    def calculate(self, price):
        return price * 0.9

class ClearanceDiscount(Discount):
    def calculate(self, price):
        return price * 0.5

def apply_discount(discount: Discount, price):
    return discount.calculate(price)

print(apply_discount(SeasonalDiscount(), 100))  # 90.0

```

🅛 — Liskov Substitution Principle (LSP)
Subclasses should be usable in place of their parent class

If class B is a subclass of class A, then objects of class A should be replaceable with objects of class B without breaking the code.

✅ Example:
If Bird has a method fly(), a Penguin subclass shouldn't break this if penguins can't fly.

```python
class Bird:
    def fly(self):
        print("Flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

class Ostrich(Bird):  # Violates LSP if it can't fly
    def fly(self):
        raise NotImplementedError("Ostriches can't fly")

# LSP-compliant approach
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        print("Flying")

class Ostrich(Bird):
    def run(self):
        print("Running")

```

🅘 — Interface Segregation Principle (ISP)
Don't force a class to implement methods it doesn't use

Break large interfaces into smaller, more specific ones so classes only implement what they need.

✅ Example:
Separate IPrinter, IScanner, and IFax instead of one big IMachine interface.

```python
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self): pass

class Scanner(ABC):
    @abstractmethod
    def scan(self): pass

class AllInOne(Printer, Scanner):
    def print(self):
        print("Printing")
    def scan(self):
        print("Scanning")

class SimplePrinter(Printer):
    def print(self):
        print("Just printing")

```

🅓 — Dependency Inversion Principle (DIP)
Depend on abstractions, not concrete classes

High-level modules should not depend on low-level modules; both should depend on interfaces or abstractions.

✅ Example:
A PaymentService should depend on a PaymentGateway interface, not directly on Stripe or PayPal.

```python

from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount): pass

class StripeGateway(PaymentGateway):
    def pay(self, amount):
        print(f"Paid ₹{amount} via Stripe")

class PaymentProcessor:
    def __init__(self, gateway: PaymentGateway):
        self.gateway = gateway

    def process(self, amount):
        self.gateway.pay(amount)

# Usage
processor = PaymentProcessor(StripeGateway())
processor.process(500)

```