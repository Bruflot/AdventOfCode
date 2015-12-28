import re

with open('input.txt', 'r') as f:
    total = 0
    buf = f.read()

    start = [m.start(0) for m in re.finditer(r'[{]', buf)]
    end = [m.start(0) for m in re.finditer(r'[}]', buf)]
    red = [m.start(0) for m in re.finditer(r'(red)', buf)]

    temp = 0
    for i in red:
        for idx, pos in enumerate(end):
            temp += 1
            temp_total = 0
            indexes = []
            for indx, a in enumerate(start):
                if 0 < pos-a < temp_total or temp_total == 0:
                    temp_total = pos-a
                    indexes = [a, pos, indx, idx]

            if not indexes[0] < i < indexes[1]:
                total += sum(int(x) for x in re.findall(r'\-?[0-9]+', buf[indexes[0]:indexes[1]]))

            start.pop(indexes[2])
            end.pop(indexes[3])

print(total)
