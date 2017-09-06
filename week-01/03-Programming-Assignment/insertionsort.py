with open('input.txt', 'r') as file_object:
    n, s = [line.strip() for line in file_object]
    sequence = list((map(int, s.split())))

index_list = [1]
for idx in range(1, int(n)):
    value = sequence[idx]
    i = idx - 1
    index = idx + 1
    while i >= 0:
        if value < sequence[i]:
            sequence[i], sequence[i+1] = value, sequence[i]
            i -= 1
            index -= 1
        else:
            break
    index_list.append(index)

with open('output.txt', 'w') as file_object:
    index_list = map(str, index_list)
    first_line = ' '.join(index_list)
    sequence = map(str, sequence)
    second_line = ' '.join(sequence)
    file_object.write(first_line + '\n')
    file_object.write(second_line + '\n')
