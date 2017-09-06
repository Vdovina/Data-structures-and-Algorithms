with open('input.txt', 'r') as file_object:
    n, s = [line.strip() for line in file_object]
    sequence = list((map(float, s.split())))

sequence = [(income, idx) for idx, income in enumerate(sequence, start=1)]
sequence.sort()
result = ' '.join(map(str, [min(sequence)[1], sequence[len(sequence) // 2][1], max(sequence)[1]]))

with open('output.txt', 'w') as file_object:
    file_object.write(result)
