import math

from algebraic import add_while, count_while


def hamming_bound(q, n, d):
    return (q ** n) / count_spheres(q, n, (d - 1) // 2)


def hamming_bound_for_n(q, k, d):
    return count_while(q ** k - 1, lambda n: hamming_bound(q, n, d), k + 1) + 1


def hamming_bound_for_k(q, n, d):
    return n - math.ceil(math.log(count_spheres(q, n, (d - 1) // 2), q))


def hamming_bound_for_d(q, n, k):
    return 2 * add_while(q ** (n - k), lambda t: math.comb(n, t) * ((q - 1) ** t))


def count_spheres(q, n, t):
    return sum([math.comb(n, i) * ((q - 1) ** i) for i in range(0, t + 1)])

