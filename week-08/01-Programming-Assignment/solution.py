s = set()

commands = {
    'A': lambda x: s.add(x),
    'D': lambda x: s.discard(x),
    '?': lambda x: write_object.write('Y\n' if x in s else 'N\n')
}

with open('input.txt', 'r') as read_object, open('output.txt', 'w') as write_object:
    n = int(read_object.readline())
    for line in read_object:
        command, key = line.strip().split()
        commands[command](key)
