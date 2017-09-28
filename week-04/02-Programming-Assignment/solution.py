from collections import deque

d = deque()

with open('input.txt', 'r') as read_object, open('output.txt', 'w') as write_object:
    n = read_object.readline()
    for line in read_object:
        if line.startswith('+'):
            d.append(line[2:])
        else:
            x = d.popleft()
            write_object.write(x)
