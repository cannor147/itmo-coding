import numpy as np

from algebraic import describe_field, vector, bi_project, hamming_distance, fsum
from algebraic.matrix import minimal_span_form


def get_active_rows(g):
    k, n = np.shape(g)
    s = [min([j if g[i][j] == 1 else n + 1 for j in range(n)]) for i in range(k)]
    t = [max([j if g[i][j] == 1 else -1 for j in range(n)]) for i in range(k)]
    return [[]] + [[i for i in range(k) if s[i] <= j < t[i]] for j in range(n)]


def get_xi(active_rows):
    return [len(active_rows[i]) for i in range(len(active_rows))]


def trellis_from_gen(g, one=1):
    msg = minimal_span_form(g)
    active_rows = get_active_rows(msg)
    xi = get_xi(active_rows)
    vertexes = [describe_field(xi[i], one=one) for i in range(len(active_rows))]

    n = len(active_rows) - 1
    intersections = [list(filter(lambda j: j in active_rows[i + 1], active_rows[i])) for i in range(n)]
    unions = [list(set(active_rows[i] + active_rows[i + 1])) for i in range(n)]
    x = [vector(list(msg[:, i])).project(unions[i]) for i in range(n)]

    edges = [[] for _ in range(n)]
    for i in range(n):
        for u in vertexes[i]:
            for v in vertexes[i + 1]:
                if u.project(intersections[i], active_rows[i]) == v.project(intersections[i], active_rows[i + 1]):
                    w = bi_project(u, active_rows[i], v, active_rows[i + 1], unions[i])
                    f = fsum(np.array(w) * np.array(x[i]))
                    edges[i].append((u, v, f))
    return edges


def decode_from_trellis(trellis, code):
    n = len(code)
    distances = [dict() for _ in range(n + 1)]
    distances[0][vector([])] = 0

    for i in range(n):
        for (u, v, f) in trellis[i]:
            d = hamming_distance([f], [code[i]])
            path_d = distances[i][u]
            if v in distances[i + 1]:
                distances[i + 1][v] = min(distances[i + 1][v], d + path_d)
            else:
                distances[i + 1][v] = d + path_d

    max_d = distances[n][vector([])]
    v = vector([])
    result = []
    for i in reversed(range(n)):
        min_u, min_d, min_f = None, max_d, None
        for (u, w, f) in trellis[i]:
            d = hamming_distance([f], [code[i]])
            if distances[i][u] + d <= min_d and w == v:
                min_d = distances[i][u] + d
                min_u = u
                min_f = f
        v = min_u
        result.append(min_f)
    return np.array(list(reversed(result)))
