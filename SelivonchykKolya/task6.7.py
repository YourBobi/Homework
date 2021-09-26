# Task 4.7
# Implement a class Money to represent value and currency.
# You need to implement methods to use all basic arithmetics expressions (comparison, division, multiplication,
# addition and subtraction). Tip: use class attribute exchange rate which is dictionary and stores information about
# exchange rates to your default currency.
from functools import total_ordering

@total_ordering
class Money:

    def __init__(self, value, currency="USD"):
        self.exchange_rate = {
            "EUR": 0.93,
            "BYN": 2.1,
            "JPY": 110.72,
            "USD": 1
        }
        if currency not in self.exchange_rate:
            raise AttributeError("unknown currency")

        self.currency = currency
        self.value = value

    def get_exchange_rate(self, currency=None):
        if currency is None:
            return self.value
        else:
            return self.value / self.exchange_rate[self.currency] * self.exchange_rate[currency]

    # comparison
    def __eq__(self, other):
        return self.get_exchange_rate() == other.get_exchange_rate()

    def __lt__(self, other):
        return self.get_exchange_rate() < other.get_exchange_rate()

    # division
    def __truediv__(self, other):
        if isinstance(other, Money):
            return Money(self.get_exchange_rate() / other.get_exchange_rate(self.currency))
        return Money(self.get_exchange_rate() / other, self.currency)

    def __rtruediv__(self, other):
        return Money(other / self.get_exchange_rate(),self.currency)

    def __floordiv__(self, other):
        if isinstance(other, Money):
            return Money(self.get_exchange_rate() // other.get_exchange_rate(self.currency), self.currency)
        return Money(self.get_exchange_rate() // other, self.currency)

    def __rfloordiv__(self, other):
        return Money(other // self.get_exchange_rate(), self.currency)

    # multiplication
    def __mul__(self, other):
        if isinstance(other, Money):
            return Money(self.get_exchange_rate() * other.get_exchange_rate(self.currency))
        return Money(self.get_exchange_rate() * other, self.currency)

    def __rmul__(self, other):
        return Money(self.get_exchange_rate() * other, self.currency)

    # addition
    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.get_exchange_rate() + other.get_exchange_rate(self.currency), self.currency)
        return Money(self.get_exchange_rate() + other)

    def __radd__(self, other):
        return Money(self.get_exchange_rate() + other, self.currency)

    # subtraction
    def __sub__(self, other):
        if isinstance(other, Money):
            return Money(self.get_exchange_rate() - other.get_exchange_rate(self.currency), self.currency)
        return Money(self.get_exchange_rate() - other, self.currency)

    def __rsub__(self, other):
        return Money(self.get_exchange_rate() - other, self.currency)

    def __repr__(self):
        return str(round(self.get_exchange_rate(), 4)) + " " + self.currency


x = Money(10, "BYN")
y = Money(11)  # define your own default value, e.g. “USD”
z = Money(12.34, "EUR")
c = Money(11.4762)
print(z + 3.11 * x + y * 0.8)
lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
s = sum(lst)
print(s)