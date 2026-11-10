"""Тема 3. Операторы ветвления: if/elif/else, логические операторы, словарь вместо switch."""


def task_13(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


def task_14(score):
    if score >= 90:
        return "отлично"
    elif score >= 75:
        return "хорошо"
    elif score >= 60:
        return "удовлетворительно"
    else:
        return "неудовлетворительно"


def task_15(age, is_citizen):
    if age >= 18 and is_citizen:
        return True
    else:
        return False


def task_16(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True

        if char.isdigit():
            has_digit = True

    if has_upper and has_digit:
        return True
    else:
        return False


def task_17(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def task_18(op, a, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return None
        else:
            return a / b
    else:
        return None
