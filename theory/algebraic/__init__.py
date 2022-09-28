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
