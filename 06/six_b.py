matrix = [[0 for x in range(0, 1000)] for y in range(0, 1000)]
total = 0

with open('six_raw.txt', 'r') as f:
    for line in f:
        line = line.replace('through', '')\
            .replace('turn', '')\
            .rstrip('\n')\
            .split()

        cmd, start, end = line
        start = list(map(int, start.split(',')))
        end = list(map(int, end.split(',')))

        for _x in range(start[0], end[0]+1):
            for _y in range(start[1], end[1]+1):
                if cmd == 'on':
                    matrix[_x][_y] += 1
                elif cmd == 'off':
                    if matrix[_x][_y] > 0:
                        matrix[_x][_y] -= 1
                else:
                    matrix[_x][_y] += 2

for column in matrix:
    for row in column:
        total += row

print(total)
