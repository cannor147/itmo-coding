import numpy as np

from algebraic import describe_field, vector, hamming_distance
from algebraic.binary import binary_array, unwrap
from algebraic.matrix import gaussian, transpose, from_permutation
from algebraic.linear.gilbert_varshamov import gilbert_varshamov_bound_for_k, gilbert_varshamov_bound_for_d, \
    gilbert_varshamov_bound_for_n
from algebraic.linear.griesmer import griesmer_bound_for_k, griesmer_bound_for_d, griesmer_bound_for_n
from algebraic.linear.hamming import hamming_bound_for_k, hamming_bound_for_d, hamming_bound_for_n
from algebraic.linear.singleton import singleton_bound_for_k, singleton_bound_for_d, singleton_bound_for_n


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


def find_n_by_gen(g):
    return np.shape(g)[1]


def find_k_by_gen(g):
    return sum([1 if np.count_nonzero(row != 0) > 0 else 0 for row in g])


def find_d_by_syndromes(syndromes):
    for e, vectors in syndromes.items():
        if sum([1 if x != 0 else 0 for x in e]) != 0:
            continue
        d = None
        for u in vectors:
            for v in vectors:
                if u == v:
                    continue
                dh = hamming_distance(u, v)
                if d is None:
                    d = dh
                elif dh < d:
                    d = dh
        return d
    return 0


def syndromes_by_check(h, one=1):
    ht = h.transpose()
    r, n = np.shape(h)

    vectors = describe_field(n, one=one)
    syndromes = dict()
    for v in vectors:
        error = vector(np.array(v) @ ht)
        if error in syndromes:
            syndromes[error].append(v)
        else:
            syndromes[error] = [v]
    return syndromes


def leaders_of_syndromes(syndromes):
    leaders = dict()
    for e in syndromes.keys():
        for v in syndromes[e]:
            if e not in leaders:
                leaders[e] = v
                continue

            weight = sum([1 if x != 0 else 0 for x in v])
            leader_weight = sum([1 if x != 0 else 0 for x in leaders[e]])
            if weight < leader_weight or (weight == leader_weight and str(v) > str(leaders[e])):
                leaders[e] = v
    return leaders


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
