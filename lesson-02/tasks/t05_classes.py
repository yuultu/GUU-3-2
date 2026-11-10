def task_25():
    class Dog:
        def __init__(self, name, breed):
            self.name = name
            self.breed = breed

        def bark(self):
            return f"Гав! Я {self.name}, порода {self.breed}"

    return Dog


Dog = task_25()


def task_26():
    class Robot:
        count = 0

        def __init__(self):
            Robot.count += 1
            self.serial = Robot.count

    return Robot


Robot = task_26()


def task_27():
    class Settings:
        def __init__(self, **options):
            for key, value in options.items():
                setattr(self, key, value)

        def get(self, key, default=None):
            return getattr(self, key, default)

    return Settings


Settings = task_27()


def task_28():
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def distance_to(self, other):
            return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

        def __repr__(self):
            return f"Point(x={self.x}, y={self.y})"

    return Point


Point = task_28()


def task_29():
    class Money:
        def __init__(self, amount, currency):
            self.amount = amount
            self.currency = currency

        def __eq__(self, other):
            if not isinstance(other, Money):
                return False
            return self.amount == other.amount and self.currency == other.currency

    return Money


Money = task_29()


def task_30():
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)

        def __mul__(self, scalar):
            return Vector(self.x * scalar, self.y * scalar)

        def magnitude(self):
            return (self.x ** 2 + self.y ** 2) ** 0.5

    return Vector


Vector = task_30()
