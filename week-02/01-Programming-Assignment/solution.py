import sys


buffer = []


def merge_sort(sequence):
    merge_sort2(sequence, 0, len(sequence) - 1)


def merge_sort2(sequence, first, last):
    if first < last:
        middle = (first + last) // 2
        merge_sort2(sequence, first, middle)
        merge_sort2(sequence, middle + 1, last)
        merge(sequence, first, middle, last)


def merge(sequence, first, middle, last):
    lhs = sequence[first:middle + 1]
    rhs = sequence[middle + 1:last + 1]
    lhs.append(sys.maxsize)
    rhs.append(sys.maxsize)
    i = j = 0
    for k in range(first, last + 1):
        if lhs[i] <= rhs[j]:
            sequence[k] = lhs[i]
            i += 1
        else:
            sequence[k] = rhs[j]
            j += 1
    buffer.append('%d %d %d %d\n' % (first+1, last+1, sequence[first], sequence[last]))

with open('input.txt', 'r') as read_object, open('output.txt', 'w') as write_object:
    n, s = [line.strip() for line in read_object]
    n = int(n)
    sequence = [int(i) for i in s.split()]

    merge_sort(sequence)

    for i in buffer:
        write_object.write(i)

    sequence = map(str, sequence)
    line = ' '.join(sequence)
    write_object.write(line + '\n')
