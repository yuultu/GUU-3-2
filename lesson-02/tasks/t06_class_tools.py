def task_31():
    class MathUtils:
        @staticmethod
        def is_even(n):
            return n % 2 == 0

        @staticmethod
        def celsius_to_fahrenheit(c):
            return c * 9 / 5 + 32

    return MathUtils


MathUtils = task_31()


def task_32():
    class Date:
        def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day

        @classmethod
        def from_string(cls, text):
            year, month, day = text.split("-")
            return cls(int(year), int(month), int(day))

    return Date


Date = task_32()


def task_33():
    class Temperature:
        def __init__(self, celsius):
            self.celsius = celsius

        @property
        def fahrenheit(self):
            return self.celsius * 9 / 5 + 32

    return Temperature


Temperature = task_33()


def task_34():
    class Account:
        def __init__(self, owner, balance=0):
            self.owner = owner
            self.balance = balance

        @property
        def balance(self):
            return self._balance

        @balance.setter
        def balance(self, value):
            if value < 0:
                raise ValueError("Баланс не может быть отрицательным")
            self._balance = value

        def deposit(self, amount):
            if amount < 0:
                raise ValueError("Сумма пополнения не может быть отрицательной")
            self.balance += amount

    return Account


Account = task_34()


def task_35():
    import math

    class Circle:
        def __init__(self, radius):
            self.radius = radius

        @property
        def area(self):
            return math.pi * self.radius ** 2

        @property
        def perimeter(self):
            return 2 * math.pi * self.radius

    return Circle


Circle = task_35()


def task_36():
    class Numbers:
        MULTIPLIER = 3.5

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def add(self):
            return self.x + self.y

        @classmethod
        def multiply(cls, a):
            return a * cls.MULTIPLIER

        @staticmethod
        def subtract(b, c):
            return b - c

        @property
        def value(self):
            return self.x, self.y

        @value.setter
        def value(self, pair):
            self.x, self.y = pair

    return Numbers


Numbers = task_36()