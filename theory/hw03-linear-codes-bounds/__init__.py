from algebraic.linear import max_k, max_d

q = 2
n = 17
d = 6

k1 = max_k(q=q, n=n, d=d, bound="hamming")
k2 = max_k(q=q, n=n, d=d, bound="griesmer")
k3 = max_k(q=q, n=n, d=d, bound="varshamov")
print(k1, k2, k3)

q = 2
n = 16
k = 9

d1 = max_d(q=q, n=n, k=k, bound="hamming")
d2 = max_d(q=q, n=n, k=k, bound="griesmer")
d3 = max_d(q=q, n=n, k=k, bound="varshamov")
print(d1, d2, d3)
