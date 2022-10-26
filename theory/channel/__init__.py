import math


def bsc_probability(x, y, p):
    return 1 - p if x == y else p


def bsc_bhattacharyya(p):
    return 2 * p - 2 * p * p


def awgnc_probability(x, y, sigma):
    return math.exp(- ((y - x) / sigma) ** 2 / 2) / math.sqrt(2 * math.pi * sigma ** 2)


def awgnc_bhattacharyya(sigma):
    return math.exp(-0.5 / (sigma * sigma))
