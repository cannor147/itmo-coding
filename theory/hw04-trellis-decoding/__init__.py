from algebraic.binary import binary_array, Binary
from algebraic.matrix import minimal_span_form
from tree.viterbi import get_active_rows, get_xi, trellis_from_gen, decode_from_trellis

g = binary_array([
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0],
])
y = binary_array([0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0])

msg = minimal_span_form(g)
active_rows = get_active_rows(msg)
xi = get_xi(active_rows)
print(xi)

trellis = trellis_from_gen(g, one=Binary(1))
x = decode_from_trellis(trellis, y)
print(x)
