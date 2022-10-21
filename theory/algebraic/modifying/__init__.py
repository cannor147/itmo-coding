import numpy as np

from algebraic.matrix import gaussian
from algebraic import fsum, inc


def augment(g, row):
    return np.append(g, [row], axis=0)


def expurgate(g, row_index):
    return np.delete(g, row_index, axis=0)


def extend(g, column):
    return np.append(g, [[x] for x in column], axis=1)


def puncture(g, column_index):
    return np.delete(g, column_index, axis=1)


def lengthen(g, column, row):
    return np.append(np.append(g, [[x] for x in column], axis=1), [row], axis=0)


def shorten(g, column_index, row_index):
    return np.delete(np.delete(g, column_index, axis=1), row_index, axis=0)


def auto_augment(g):
    zero = g[0][0] - g[0][0]
    one = zero + 1
    n = np.shape(g)[1]
    row = np.array([one if i == 0 else zero for i in range(n)])
    while fsum(row) > 0:
        result = augment(g, row)
        if gaussian(result)[0] is not None:
            return result
        inc(row, one=one)
    return g


def auto_expurgate(g):
    k, n = np.shape(g)
    for i in range(k):
        result = expurgate(g, i)
        for j in range(n):
            if fsum(result[:, j]) == 0:
                continue
        return result
    return g


def auto_extend(g):
    k = np.shape(g)[0]
    return extend(g, [fsum(g[i]) for i in range(k)])


def auto_puncture(g):
    n = np.shape(g)[1]
    for i in range(n):
        result = puncture(g, i)
        if gaussian(result)[0] is not None:
            return result
    return g


def auto_lengthen(g):
    zero = g[0][0] - g[0][0]
    one = zero + 1
    k, n = np.shape(g)
    return lengthen(g, np.array([zero for _ in range(k)]), np.array([one for _ in range(n + 1)]))


def auto_shorten(g):
    result = auto_expurgate(auto_puncture(g))
    k, n = np.shape(g)
    k0, n0 = np.shape(result)
    return result if k0 + 1 == k and n0 + 1 == n else g
