"""Домашнее задание. Тема 1: основы Python (строки, числа, форматирование)."""


def hw_01(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return f"{hours:02}:{minutes:02}:{seconds:02}"


def hw_02(a, b, c):
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

    return round(area, 2)


def hw_03(card_number):
    if len(card_number) <= 4:
        return card_number

    return "*" * (len(card_number) - 4) + card_number[-4:]


def hw_04(x, y):
    result = x / y
    return f"{x} / {y} = {result:.2f}"