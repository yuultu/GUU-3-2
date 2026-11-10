"""Домашнее задание. Тема 5: циклы."""


def hw_15(n):
    result = []

    a = 0
    b = 1

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result


def hw_16(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def hw_17(n):
    result = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("fizzbuzz")
        elif i % 3 == 0:
            result.append("fizz")
        elif i % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(i))

    return result
