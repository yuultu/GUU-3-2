def task_07(*args):
    result = 1
    for arg in args:
        result *= arg
    return result


def task_08(**kwargs):
    return "; ".join(
        f"{key}={value}"
        for key, value in sorted(kwargs.items())
    )


def task_09(func, args, kwargs):
    return func(*args, **kwargs)


def task_10(words):
    return sorted(words, key=lambda word: (len(word), word))


def task_11(numbers):
    return list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))


def task_12(f, g):
    return lambda x: f(g(x))