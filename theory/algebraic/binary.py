import numpy as np


class Binary:
    def __init__(self, value):
        self.value = 0 if value == 0 else 1

    def __add__(self, other):
        return self ^ other

    def __neg__(self):
        return Binary(self.value)

    def __sub__(self, other):
        return self ^ other

    def __mul__(self, other):
        return self & other

    def __divmod__(self, other):
        return Binary(self.value.__divmod__(other.value)) if is_binary(other) else self.__divmod__(Binary(other))

    def __invert__(self):
        return Binary(1 if self.value == 0 else 0)

    def __or__(self, other):
        return Binary(self.value | other.value) if is_binary(other) else self | Binary(other)

    def __xor__(self, other):
        return Binary(self.value ^ other.value) if is_binary(other) else self ^ Binary(other)

    def __and__(self, other):
        return Binary(self.value & other.value) if is_binary(other) else self & Binary(other)

    def __str__(self):
        return self.value.__str__()

    def __repr__(self):
        return self.value.__repr__()

    def __eq__(self, other):
        return self.value == other.value if is_binary(other) else self.value == other

    def __ne__(self, other):
        return self.value != other.value if is_binary(other) else self.value != other

    def __lt__(self, other):
        return self.value < other.value if is_binary(other) else self.value < other

    def __le__(self, other):
        return self.value <= other.value if is_binary(other) else self.value <= other

    def __gt__(self, other):
        return self.value > other.value if is_binary(other) else self.value > other

    def __ge__(self, other):
        return self.value >= other.value if is_binary(other) else self.value >= other


def is_binary(value):
    return isinstance(value, Binary)


def unwrap(value):
    return value.value if is_binary(value) else value


def binary_array(arr):
    return np.array([binary_array(x) if isinstance(x, np.ndarray) or isinstance(x, list) else Binary(x) for x in arr])


def to_array(arr):
    return np.array([to_array(x) if isinstance(x, np.ndarray) or isinstance(x, list) else unwrap(x) for x in arr])
