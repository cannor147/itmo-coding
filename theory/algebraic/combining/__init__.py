from algebraic.binary import binary_array

import numpy as np


def plotkin_construction(g1, g2):
    k1, n1 = np.shape(g1)
    k2, n2 = np.shape(g2)
    k, n = k1 + k2, n1 + n2
    if n1 != n2 or k1 == 0 or k2 == 0 or n1 == 0:
        return None
    zero = g1[0][0] - g1[0][0]
    result = [[g1[i - k2][j % n1] if i >= k2 else g2[i][j] if j < n1 else zero for j in range(n)] for i in range(k)]
    return np.array(result)


def kron(g1, g2):
    return np.kron(g1, g2)


def reed_muller(r, m):
    n = 2 ** m
    if r > m or r < 0:
        return None
    if r == 0:
        return binary_array([[1 for _ in range(n)]])
    if r == m:
        return binary_array([[1 if i == j else 0 for j in range(n)] for i in range(n)])
    return plotkin_construction(reed_muller(r, m - 1), reed_muller(r - 1, m - 1))
