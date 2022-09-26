import numpy as np

from algebra.binary import binary_array
from algebra.matrix import gaussian, transpose, from_permutation
from coding.linear.gilbert_varshamov import gilbert_varshamov_bound_for_k, gilbert_varshamov_bound_for_d, \
    gilbert_varshamov_bound_for_n
from coding.linear.griesmer import griesmer_bound_for_k, griesmer_bound_for_d, griesmer_bound_for_n
from coding.linear.hamming import hamming_bound_for_k, hamming_bound_for_d, hamming_bound_for_n
from coding.linear.singleton import singleton_bound_for_k, singleton_bound_for_d, singleton_bound_for_n


def gen_to_check(g):
    n = len(g[0])
    k = len(g)

    (gs, p) = gaussian(g)
    s = gs[:, k:n]

    hs = np.append(-transpose(s), np.identity(k), axis=1)
    return np.dot(hs, from_permutation(p))


def check_to_gen(h):
    n = len(h[0])
    k = n - len(h)

    (hs, p) = gaussian(h)
    hs = np.roll(hs, k - n, axis=1)
    p = np.roll(p, k - n)
    s = hs[:, 0:n - k]

    gs = np.append(binary_array(np.identity(k)), -transpose(s), axis=1)
    return np.dot(gs, from_permutation(p))


def min_n(q, k, d, bound):
    if bound == "singleton":
        return singleton_bound_for_n(k=k, d=d)
    if bound == "hamming":
        return hamming_bound_for_n(q=q, k=k, d=d)
    if bound == "griesmer" and q == 2:
        return griesmer_bound_for_n(k=k, d=d)
    if bound == "gilbert" or bound == "varshamov" or bound == "gilbert-varshamov" or bound == "gilbert_varshamov":
        return gilbert_varshamov_bound_for_n(q=q, k=k, d=d)
    return None


def max_k(q, n, d, bound):
    if bound == "singleton":
        return singleton_bound_for_k(n=n, d=d)
    if bound == "hamming":
        return hamming_bound_for_k(q=q, n=n, d=d)
    if bound == "griesmer" and q == 2:
        return griesmer_bound_for_k(n=n, d=d)
    if bound == "gilbert" or bound == "varshamov" or bound == "gilbert-varshamov" or bound == "gilbert_varshamov":
        return gilbert_varshamov_bound_for_k(q=q, n=n, d=d)
    return None


def max_d(q, n, k, bound):
    if bound == "singleton":
        return singleton_bound_for_d(n=n, k=k)
    if bound == "hamming":
        return hamming_bound_for_d(q=q, n=n, k=k)
    if bound == "griesmer" and q == 2:
        return griesmer_bound_for_d(n=n, k=k)
    if bound == "gilbert" or bound == "varshamov" or bound == "gilbert-varshamov" or bound == "gilbert_varshamov":
        return gilbert_varshamov_bound_for_d(q=q, n=n, k=k)
    return None
