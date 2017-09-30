def check(s):
    stack = []
    if s[0] in (')', ']'):
        return False
    for i in range(len(s)):
        if s[i] in ('(', '['):
            stack.append(s[i])
        else:
            if s[i] == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            elif s[i] == ']' and len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return True if len(stack) == 0 else False


with open('input.txt', 'r') as read_object, open('output.txt', 'w') as write_object:
    n = read_object.readline()
    for line in read_object:
        line = line.strip()
        write_object.write('YES\n' if check(line) else 'NO\n')
