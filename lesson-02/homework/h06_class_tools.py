def hw_18():
    class Employee:
        def __init__(self, name, age, role):
            self.name = name
            self.age = age
            self.role = role

        @classmethod
        def from_string(cls, text):
            name, age, role = text.split(";")
            return cls(name, int(age), role)

    return Employee


Employee = hw_18()


def hw_19():
    class Password:
        def __init__(self, raw):
            self._password = raw

        @property
        def password(self):
            return "*" * len(self._password)

        @property
        def is_strong(self):
            return (
                len(self._password) >= 8
                and any(char.isupper() for char in self._password)
                and any(char.isdigit() for char in self._password)
            )

        def check(self, candidate):
            return self._password == candidate

    return Password


Password = hw_19()


def hw_20():
    class Stats:
        def __init__(self, values):
            self.values = list(values)

        def __len__(self):
            return len(self.values)

        def __getitem__(self, index):
            return self.values[index]

        def mean(self):
            if not self.values:
                return None
            return sum(self.values) / len(self.values)

    return Stats


Stats = hw_20()
