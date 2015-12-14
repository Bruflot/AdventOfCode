def three_a():
    x, y = 0, 0
    houses = set()

    with open('three_raw.txt', 'r') as f:
        for char in f.read():
            if char is '<':
                x -= 1
            elif char is '>':
                x += 1
            elif char is '^':
                y += 1
            elif char is 'v':
                y -= 1
            houses.add((x, y))

    print(len(houses))