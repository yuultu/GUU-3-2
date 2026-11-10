"""Домашнее задание. Тема 2: переменные, mutable/immutable, замыкания."""


def hw_05():
    total = 0

    def accumulator(value):
        nonlocal total
        total += value
        return total

    return accumulator


def hw_06(settings, defaults):
    result = defaults.copy()
    result.update(settings)

    return result