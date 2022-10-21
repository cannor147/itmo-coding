class vector(list):
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '*' if len(self) == 0 else ''.join(map(str, self))

    def __hash__(self):
        return self.__str__().__hash__()

    def __eq__(self, other):
        return len(self) == len(other) and sum([0 if self[i] == other[i] else 1 for i in range(len(self))]) == 0

    def project(self, projection, coordinates=None):
        coordinates = range(len(self)) if coordinates is None or len(coordinates) != len(self) else coordinates
        result = vector([])
        for p in projection:
            f = False
            for i in range(len(self)):
                if coordinates[i] == p:
                    result.append(self[i])
                    f = True
                    break
            if not f:
                result.append(None)
        return result


def hamming_distance(u, v):
    return abs(len(u) - len(v)) + sum([0 if u[i] == v[i] else 1 for i in range(min(len(u), len(v)))])


def bi_project(u, u_coordinates, v, v_coordinates, projection):
    return vector(u + v).project(projection, coordinates=u_coordinates + v_coordinates)


def describe_field(k, one=1):
    zero = one - one
    v = vector([zero for _ in range(k)])
    result = [v]

    u = vector(v.copy())
    inc(u, one=one)
    while u != v:
        result.append(vector(u.copy()))
        inc(u, one=one)
    return result


def fsum(v):
    res = 0
    for x in v:
        res = x + res
    return res


def inc(v, one=1):
    for i in range(len(v)):
        old = v[i]
        v[i] += one
        if old < v[i]:
            break
    return v


def add_while(max_count, addition, initial_value=0):
    t = initial_value
    count = 0
    while count <= max_count:
        count += addition(t)
        t += 1
    return t - 1


def count_while(max_count, calculation, initial_value=0):
    t = initial_value
    while calculation(t) <= max_count:
        t += 1
    return t - 1
