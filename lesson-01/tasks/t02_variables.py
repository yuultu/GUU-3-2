"""Тема 2. Переменные и область видимости: типы, mutable/immutable, константы, замыкания."""

# Константа модуля: налог на продажу. Используйте её в task_08.
TAX_RATE = 0.20


def task_07(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return (minimum, maximum)


def task_08(total):
    result = total * (1 + TAX_RATE)
    return round(result, 2)


def task_09(items, item):
    new_items = items.copy()
    new_items.append(item)
    return new_items


def task_10(values):
    result = []

    for value in values:
        number = int(value)
        result.append(number)

    return result


def task_11(k):
    def multiplier(x):
        return x * k

    return multiplier


def task_12(box, key, value):
    box[key] = value
    return box
