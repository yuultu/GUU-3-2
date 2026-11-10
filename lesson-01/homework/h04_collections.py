"""Домашнее задание. Тема 4: коллекции."""


def hw_11(text):
    words = text.split()

    if not words:
        return ""

    word = words[0]
    count = 0

    for w in words:
        current = 0

        for x in words:
            if x == w:
                current += 1

        if current > count:
            count = current
            word = w

    return word


def hw_12(matrix):
    result = []

    for row in matrix:
        result.append(sum(row))

    return result


def hw_13(items):
    result = []

    for item in items:
        if item not in result:
            result.append(item)

    return result


def hw_14(mapping):
    result = {}

    for key in mapping:
        value = mapping[key]
        result[value] = key

    return result
