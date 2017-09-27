stack = []

with open('input.txt', 'r') as read_object, open('output.txt', 'w') as write_object:
    n = read_object.readline()
    for line in read_object:
        if line.startswith('+'):
            stack.append(line[2:])
        else:
            x = stack.pop()
            write_object.write(x)
