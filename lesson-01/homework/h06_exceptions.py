"""Домашнее задание. Тема 6: ошибки и исключения."""


def hw_18(text):
    try:
        parts = text.split()

        if len(parts) != 2:
            return None

        a = int(parts[0])
        b = int(parts[1])

        return (a, b)
    except ValueError:
        return None


def hw_19(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            result = []

            for line in file:
                result.append(line.rstrip("\n"))

            return result
    except FileNotFoundError:
        return []


def hw_20(age):
    if not isinstance(age, int):
        raise TypeError("возраст должен быть целым числом")

    if age < 0 or age > 120:
        raise ValueError("возраст должен быть от 0 до 120")

    return age
