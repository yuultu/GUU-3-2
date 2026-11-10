def hw_08(func):
    called = False

    def wrapper(*args, **kwargs):
        nonlocal called
        if called:
            raise RuntimeError("Функция уже была вызвана")
        called = True
        return func(*args, **kwargs)

    return wrapper


def hw_09(*types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, (arg, expected_type) in enumerate(zip(args, types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Неверный тип аргумента {i + 1}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


def hw_10(func):
    def wrapper(*args, **kwargs):
        wrapper.log.append(args)
        return func(*args, **kwargs)

    wrapper.log = []
    return wrapper