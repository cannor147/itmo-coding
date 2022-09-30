import numpy as np

from algebraic.binary import to_array


def transpose(mt):
    return mt.transpose() if isinstance(mt, np.ndarray) else transpose(np.array(mt))


def invert(mt):
    return np.linalg.inv(to_array(mt)) if isinstance(mt, np.ndarray) else transpose(np.array(mt))


def from_permutation(p):
    return np.array([[1 if p[i] == j else 0 for j in range(len(p))] for i in range(len(p))])


def project(vector, projector):
    return np.array([vector[position] for position in projector])


def gaussian(mt):
    n = len(mt)
    m = len(mt[0])
    k = min(n, m)

    p = np.array(range(m))
    mc = np.copy(mt)
    for i in range(k):
        if mc[i][i] == 0:
            f = False
            for j in range(i + 1, m):
                if mc[i][j] != 0:
                    mc[:, i], mc[:, j] = mc[:, j], mc[:, i].copy()
                    p[i], p[j] = p[j], p[i]
                    f = True
                    break
            if not f:
                for j in range(i + 1, n):
                    if mc[j][i] != 0:
                        mc[i] += mc[j]
                        f = True
                        break
            if not f:
                return None, None
        if mc[i][i] != 1:
            mc[i] /= mc[i][i]
        for j in range(i + 1, k):
            mc[j] -= mc[i] * mc[j][i]
    for i in range(k - 1, -1, -1):
        for j in range(i):
            mc[j] -= mc[i] * mc[j][i]
    return mc, p
