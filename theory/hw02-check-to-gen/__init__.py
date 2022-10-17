from algebraic import describe_field, vector
from algebraic.binary import binary_array, Binary
from algebraic.linear import check_to_gen, find_k_by_gen, find_n_by_gen, leaders_of_syndromes, syndromes_by_check, \
    find_d_by_syndromes
from algebraic.matrix import minimal_form

h = binary_array([
    [1, 1, 1, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]
])

g = minimal_form(check_to_gen(h))

errors = describe_field(len(g), one=Binary(1))
syndromes = syndromes_by_check(h, one=Binary(1))
leaders = leaders_of_syndromes(syndromes)

n = find_n_by_gen(g)
k = find_k_by_gen(g)
d = find_d_by_syndromes(syndromes)

print("n =", n)
print("k =", k)
print("d =", d)

print("g:")
for row in g:
    print(vector(row))

for i in range(len(errors)):
    print("T(", errors[i], ") =", leaders[errors[i]])
