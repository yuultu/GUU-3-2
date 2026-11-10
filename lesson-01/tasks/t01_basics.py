"""Тема 1. Основы Python: числа, строки, выражения, форматирование."""


def task_01(a, b, c):
    """Среднее арифметическое трёх чисел."""
    return float((a + b + c) / 3)


def task_02(total_seconds):
    """Разложить количество секунд на часы, минуты и секунды."""
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds


def task_03(fahrenheit):
    """Перевести температуру из градусов Фаренгейта в градусы Цельсия."""
    return float((fahrenheit - 32) * 5 / 9)


def task_04(price, discount_percent):
    """Цена со скидкой."""
    return round(price * (1 - discount_percent / 100), 2)


def task_05(x, y):
    """Строка-отчёт о сумме двух чисел."""
    return f"{x} + {y} = {x + y}"


def task_06(name):
    """Нормализовать имя."""
    return " ".join(word.capitalize() for word in name.split())
Desktop\lesson-01\tests