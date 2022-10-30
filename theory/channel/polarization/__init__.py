import numpy as np


def polar_probability(p, m, left_func, right_func):
    if m <= 0:
        return np.array([p])
    return np.array([[left_func(r), right_func(r)] for r in bec_polar_probability(p, m - 1)]).flatten()


def bec_polar_probability(p, m):
    return polar_probability(p, m, lambda r: 2 * r - r * r, lambda r: r * r)
