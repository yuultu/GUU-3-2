"""Тема 6. Ошибки и исключения: try/except, raise, with."""


def task_31(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def task_32(text):
    try:
        return int(text)
    except ValueError:
        return None


def task_33(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.readline().rstrip("\n")
    except FileNotFoundError:
        return ""


def task_34(n):
    if n < 0:
        raise ValueError("Число должно быть неотрицательное")

    return n


def task_35(items, index):
    try:
        return items[index]
    except IndexError:
        return "индекс вне диапазона"


def task_36(text):
    try:
        return int(text)
    except ValueError:
        try:
            return float(text)
        except ValueError:
            return None
