def singleton_bound(q, n, d):
    return q ** (n - d + 1)


def singleton_bound_for_n(k, d):
    return k + d - 1


def singleton_bound_for_k(n, d):
    return n - d + 1


def singleton_bound_for_d(n, k):
    return n - k + 1
