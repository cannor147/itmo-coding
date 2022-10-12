import math

from algebraic import add_while, count_while


def gilbert_varshamov_bound(q, n, d):
    return q ** gilbert_varshamov_bound_for_k(q, n, d)


def gilbert_varshamov_bound_for_n(q, k, d):
    return count_while(0, lambda n: q ** (n - k) - sum([calculate_addendum(q, n, i) for i in range(0, d - 1)]), k + 1)


def gilbert_varshamov_bound_for_k(q, n, d):
    return math.ceil(n - math.log(sum([calculate_addendum(q, n, i) for i in range(0, d - 1)]), q) - 1)


def gilbert_varshamov_bound_for_d(q, n, k):
    return add_while(q ** (n - k) - 1, lambda d: calculate_addendum(q, n, d)) + 1


def calculate_addendum(q, n, i):
    return math.comb(n - 1, i) * ((q - 1) ** i)
