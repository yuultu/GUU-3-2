def task_01(base, exponent=2):
    return base ** exponent


def task_02(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


def task_03(n):
    if n == 0:
        return 0
    return n + task_03(n - 1)


def task_04(item, items=None):
    result = [] if items is None else items.copy()
    result.append(item)
    return result


def task_05(name, *, greeting="Привет", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"


def task_06(func, value):
    return func(func(value))