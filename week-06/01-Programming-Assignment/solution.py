def binary_search(a, lhs, rhs, x):
    n = len(a)
    l = lhs
    r = rhs
    while r > l + 1:
        m = (r + l) // 2
        if a[m] < x:
            l = m
        else:
            r = m
    if r < n and a[r] == x:
        first = r
        last = r
        while last < n and a[last] == x:
            last += 1
        return first + 1, last
    else:
        return -1, -1


with open('input.txt', 'r') as read_object, open('output.txt', 'w') as write_object:
    n = int(read_object.readline())
    sequence = [int(i) for i in read_object.readline().split()]
    m = read_object.readline()
    tests = [int(i) for i in read_object.readline().split()]

    buffer = []
    cache = {}

    for i in tests:
        if i in cache:
            result = cache.get(i)
            buffer.append('%d %d\n' % (result[0], result[1]))
        else:
            start = -1
            result = binary_search(sequence, start, n, i)

            buffer.append('%d %d\n' % (result[0], result[1]))
            cache[i] = result

    for i in buffer:
        write_object.write(i)
