"""Тема 2. Переменные и область видимости: типы, mutable/immutable, константы, замыкания."""

# Константа модуля: налог на продажу. Используйте её в task_08.
TAX_RATE = 0.20


def task_07(numbers):
    """Минимум и максимум списка."""
    return min(numbers), max(numbers)


def task_08(total):
    """Цена с налогом."""
    return round(total * (1 + TAX_RATE), 2)


def task_09(items, item):
    """Новый список с добавленным элементом."""
    return items + [item]


def task_10(values):
    """Список строк → список целых чисел."""
    return [int(v) for v in values]


def task_11(k):
    """Фабрика функций-умножителей (замыкание)."""
    return lambda x: x * k


def task_12(box, key, value):
    """Изменение словаря по ссылке."""
    box[key] = value
    return box
