"""Домашнее задание. Тема 3: операторы ветвления."""


def hw_07(month):
    if month in (12, 1, 2):
        return "зима"
    elif month in (3, 4, 5):
        return "весна"
    elif month in (6, 7, 8):
        return "лето"
    elif month in (9, 10, 11):
        return "осень"
    else:
        return None


def hw_08(p1, p2):
    if p1 == p2:
        return "ничья"

    if p1 == "камень" and p2 == "ножницы":
        return "игрок 1"
    elif p1 == "ножницы" and p2 == "бумага":
        return "игрок 1"
    elif p1 == "бумага" and p2 == "камень":
        return "игрок 1"
    else:
        return "игрок 2"


def hw_09(a, b, c):
    return (
        a > 0 and b > 0 and c > 0
        and a + b > c
        and a + c > b
        and b + c > a
    )


def hw_10(n):
    if n % 100 in (11, 12, 13, 14):
        return "лет"

    if n % 10 == 1:
        return "год"
    elif n % 10 in (2, 3, 4):
        return "года"
    else:
        return "лет"
