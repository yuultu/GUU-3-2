"""Тема 4. Коллекции: списки, кортежи, множества, словари, строки, 2D-структуры."""


def task_19(numbers):
    result = numbers.copy()
    result.sort(reverse=True)
    return result


def task_20(items):
    if len(items) < 3:
        return ()

    result = items[1:-1]
    return result


def task_21(a, b):
    union = sorted(list(a | b))
    intersection = sorted(list(a & b))
    a_minus_b = sorted(list(a - b))

    result = {
        "union": union,
        "intersection": intersection,
        "a_minus_b": a_minus_b
    }

    return result


def task_22(text):
    words = text.split()
    result = {}

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result


def task_23(text):
    text = text.lower()
    cleaned = ""

    for char in text:
        if char.isalnum():
            cleaned += char

    return cleaned == cleaned[::-1]


def task_24(matrix):
    total = 0

    for i in range(len(matrix)):
        total += matrix[i][i]

    return total