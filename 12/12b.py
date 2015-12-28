import re

with open('input.txt', 'r') as f:
    total = 0
    buf = f.read()
    braces = []
    i = 0

    for idx, char in enumerate(buf):
        if char == '{':
            braces.append(idx)
            i += 1
        elif char == '}':
            braces[i] = [braces[i], idx]
            i -= 1

    for i in braces:
        if 'red' in buf[i[0]:i[1]]:
            print('yah')
        # if it's not, add the numbers to total
