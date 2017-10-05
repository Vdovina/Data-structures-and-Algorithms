def is_heap(heap, size):
    for i in range(1, size // 2):
        if not((2 * i <= size and heap[i] <= heap[2 * i]) and (2 * i + 1 <= size and heap[i] <= heap[2 * i + 1])):
            return False
    return True


with open('input.txt', 'r') as read_object, open('output.txt', 'w') as write_object:
    n = read_object.readline()
    h = [0]
    [h.append(int(i)) for i in read_object.readline().split()]
    write_object.write('YES' if is_heap(h, int(n)) else 'NO')
