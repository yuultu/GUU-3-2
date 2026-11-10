def hw_11(n):
    for num in range(2, n + 1):
        is_prime = True
        for divisor in range(2, num):
            if divisor * divisor > num:
                break
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            yield num


def hw_12(items, times):
    items = list(items)
    for _ in range(times):
        for item in items:
            yield item


def hw_13(items, size):
    if size <= 0:
        raise ValueError("size должен быть положительным")
    chunk = []
    for item in items:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def hw_14(items):
    iterator = iter(items)
    try:
        previous = next(iterator)
    except StopIteration:
        return
    for current in iterator:
        yield (previous, current)
        previous = current
