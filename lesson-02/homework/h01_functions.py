def hw_01(*args):
    if not args:
        return 0
    return sum(args) / len(args)


def hw_02(n):
    if n == 0 or n == 1:
        return n
    return hw_02(n - 1) + hw_02(n - 2)


def hw_03(tag, *items, sep=", "):
    return f"{tag}: {sep.join(map(str, items))}"


def hw_04(prefix, **kwargs):
    return {
        key: value
        for key, value in kwargs.items()
        if key.startswith(prefix)
    }
