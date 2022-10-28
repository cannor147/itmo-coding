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


def row_echelon_form(mt):
    n, k = np.shape(mt)
    mc = np.copy(mt)

    j = 0
    for i in range(n):
        while j < k:
            if mc[i][j] == 0:
                for p in range(i + 1, n):
                    if mc[p][j] != 0:
                        mc[i] += mc[p]
                        break
            if mc[i][j] != 0:
                break
            j += 1
        if j >= k:
            break

        if mc[i][j] != 1:
            mc[i] /= mc[i][j]
        for p in range(i + 1, n):
            mc[p] -= mc[i] * mc[p][j]
        j += 1
    return mc


def permutation_form(mt, clean=False):
    n, k = np.shape(mt)
    mc = np.copy(mt)

    used_rows = set()
    for j in range(k):
        for i in range(n):
            if i in used_rows or mc[i][j] == 0:
                continue
            used_rows.add(i)

            if mc[i][j] != 1:
                mc[i] /= mc[i][j]
            for p in range(i + 1, n):
                mc[p] -= mc[i] * mc[p][j]
            if clean:
                for p in range(0, i):
                    mc[p] -= mc[i] * mc[p][j]
            break
    return mc


def minimal_span_form(mt):
    return np.flip(permutation_form(np.flip(row_echelon_form(mt))))


def minimal_form(mt):
    return np.array(sorted(permutation_form(mt, clean=True), key=lambda x: tuple(x != 0), reverse=True))


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


def hadamard_matrix(m, positive=1, negative=-1):
    if m <= 0:
        return np.array([[positive]])
    elif m == 1:
        return np.array([[positive, negative], [positive, positive]])

    h = m // 2
    return np.kron(hadamard_matrix(h, positive, negative), hadamard_matrix(m - h, positive, negative))
