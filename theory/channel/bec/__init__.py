def bec_probability(x, y, p):
    return p if y == 'ϵ' else 1 - p if x == y else 0


def bec_bhattacharyya(p):
    return p