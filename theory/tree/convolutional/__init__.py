import numpy as np

from algebraic import fsum


def encode_convolutional(g, x):
    k, n, m = np.shape(g)
    m -= 1
    v = x if len(np.shape(x)) > 1 else [x]
    return np.array([[
        fsum([fsum(g[i][j][:m] * v[i][p:p + m] + g[i][j][m]) for i in range(k)]) for j in range(n)
    ] for p in range(np.shape(v)[1] - m + 1)])
