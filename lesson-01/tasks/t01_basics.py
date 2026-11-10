"""Тема 1. Основы Python: числа, строки, выражения, форматирование."""


def task_01(a, b, c):
    avg = (a + b + c) / 3
    return avg


def task_02(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return (hours, minutes, seconds)


def task_03(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def task_04(price, discount_percent):
    discount = price * discount_percent / 100
    final_price = price - discount
    return round(final_price, 2)


def task_05(x, y):
    total = x + y
    result = f"{x} + {y} = {total}"
    return result


def task_06(name):
    name = name.strip()
    words = name.split()
    result = ""

    for word in words:
        word = word.lower()
        word = word[0].upper() + word[1:]

        if result == "":
            result = word
        else:
            result = result + " " + word

    return result
