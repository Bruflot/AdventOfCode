import re

with open('input.txt', 'r') as f:
    total = 0
    buf = f.read()
    braces = []
    result = []
    i = 0

    for idx, char in enumerate(buf):
        if char == '{':
            braces.append(idx)
        elif char == '}':
            result.append([braces[-1], idx])

    for i in result:
        temp = buf[i[0]:i[1]]
        if 'red' not in temp:
            total += sum(int(x) for x in re.findall(r'\-?[0-9]+', temp))

print(total)
