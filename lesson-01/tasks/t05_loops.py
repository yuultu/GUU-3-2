"""Тема 5. Операторы управления циклом: while, for, break/continue, генераторы списков."""


def task_25(n):
    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10

    return total


def task_26(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def task_27(n):
    result = []

    for i in range(n):
        row = []

        for j in range(n):
            row.append((i + 1) * (j + 1))

        result.append(row)

    return result


def task_28(names, days):
    result = {}

    for name, day in zip(names, days):
        result[name] = day

    return result


def task_29(numbers):
    return [number * number for number in numbers if number % 2 == 0]


def task_30(numbers, stop_value):
    total = 0

    for number in numbers:
        if number == stop_value:
            break

        total += number

    return total