import math


def awgnc_probability(x, y, sigma):
    return math.exp(- ((y - x) / sigma) ** 2 / 2) / math.sqrt(2 * math.pi * sigma ** 2)


def awgnc_bhattacharyya(sigma):
    return math.exp(-0.5 / (sigma * sigma))