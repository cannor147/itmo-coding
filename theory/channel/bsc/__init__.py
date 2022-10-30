def bsc_probability(x, y, p):
    return 1 - p if x == y else p


def bsc_bhattacharyya(p):
    return 2 * p - 2 * p * p