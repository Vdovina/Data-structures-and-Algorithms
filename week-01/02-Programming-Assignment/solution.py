with open('input.txt', 'r') as file_object:
    s = file_object.read()
    a, b = map(int, s.split())

with open('output.txt', 'w') as file_object:
    file_object.write(str(a + b ** 2))
