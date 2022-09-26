from coding.linear.gilbert_varshamov import gilbert_varshamov_bound_for_k, gilbert_varshamov_bound_for_d, \
    gilbert_varshamov_bound_for_n
from coding.linear.griesmer import griesmer_bound_for_k, griesmer_bound_for_d, griesmer_bound_for_n
from coding.linear.hamming import hamming_bound_for_k, hamming_bound_for_d, hamming_bound_for_n
from coding.linear.singleton import singleton_bound_for_k, singleton_bound_for_d, singleton_bound_for_n


def min_n(q, k, d, bound="hamming"):
    if bound == "singleton":
        return singleton_bound_for_n(k=k, d=d)
    if bound == "hamming":
        return hamming_bound_for_n(q=q, k=k, d=d)
    if bound == "griesmer" and q == 2:
        return griesmer_bound_for_n(k=k, d=d)
    if bound == "gilbert" or bound == "varshamov" or bound == "gilbert-varshamov" or bound == "gilbert_varshamov":
        return gilbert_varshamov_bound_for_n(q=q, k=k, d=d)
    return None


def max_k(q, n, d, bound="hamming"):
    if bound == "singleton":
        return singleton_bound_for_k(n=n, d=d)
    if bound == "hamming":
        return hamming_bound_for_k(q=q, n=n, d=d)
    if bound == "griesmer" and q == 2:
        return griesmer_bound_for_k(n=n, d=d)
    if bound == "gilbert" or bound == "varshamov" or bound == "gilbert-varshamov" or bound == "gilbert_varshamov":
        return gilbert_varshamov_bound_for_k(q=q, n=n, d=d)
    return None


def max_d(q, n, k, bound="hamming"):
    if bound == "singleton":
        return singleton_bound_for_d(n=n, k=k)
    if bound == "hamming":
        return hamming_bound_for_d(q=q, n=n, k=k)
    if bound == "griesmer" and q == 2:
        return griesmer_bound_for_d(n=n, k=k)
    if bound == "gilbert" or bound == "varshamov" or bound == "gilbert-varshamov" or bound == "gilbert_varshamov":
        return gilbert_varshamov_bound_for_d(q=q, n=n, k=k)
    return None
