def task_19(n):
    for i in range(1, n + 1):
        yield i * 2


def task_20(n):
    for i in range(n, -1, -1):
        yield i


def task_21(n):
    return (i ** 2 for i in range(1, n + 1))


def task_22():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def task_23(items):
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
            yield item


def task_24(nested):
    for items in nested:
        yield from items