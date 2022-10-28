import math

import numpy as np


def polar_probability(p, m, left_func, right_func):
    if m <= 0:
        return np.array([p])
    return np.array([[left_func(r), right_func(r)] for r in bec_polar_probability(p, m - 1)]).flatten()


def bsc_probability(x, y, p):
    return 1 - p if x == y else p


def bsc_bhattacharyya(p):
    return 2 * p - 2 * p * p


def bec_probability(x, y, p):
    return p if y == 'ϵ' else 1 - p if x == y else 0


def bec_bhattacharyya(p):
    return p


def bec_polar_probability(p, m):
    return polar_probability(p, m, lambda r: 2 * r - r * r, lambda r: r * r)


def awgnc_probability(x, y, sigma):
    return math.exp(- ((y - x) / sigma) ** 2 / 2) / math.sqrt(2 * math.pi * sigma ** 2)


def awgnc_bhattacharyya(sigma):
    return math.exp(-0.5 / (sigma * sigma))
