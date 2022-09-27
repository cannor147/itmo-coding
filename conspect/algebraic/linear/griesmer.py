import math

from algebraic import add_while, count_while


def griesmer_bound(k, d):
    return sum([math.ceil(d / (2 ** i)) for i in range(0, k)])


def griesmer_bound_for_n(k, d):
    return griesmer_bound(k, d)


def griesmer_bound_for_k(n, d):
    return add_while(n, lambda k: math.ceil(d / (2 ** k)))


def griesmer_bound_for_d(n, k):
    return count_while(n, lambda d: griesmer_bound(k, d))
