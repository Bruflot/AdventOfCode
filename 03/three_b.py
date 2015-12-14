def three_b():
    s_x, s_y = 0, 0
    r_x, r_y = 0, 0
    houses = [set(), set()]

    with open('three_raw.txt', 'r') as f:
        for index, char in enumerate(f.read()):
            if index % 2 == 0:
                if char is '<':
                    s_x -= 1
                elif char is '>':
                    s_x += 1
                elif char is '^':
                    s_y += 1
                elif char is 'v':
                    s_y -= 1
                houses[0].add((s_x, s_y))
            else:
                if char is '<':
                    r_x -= 1
                elif char is '>':
                    r_x += 1
                elif char is '^':
                    r_y += 1
                elif char is 'v':
                    r_y -= 1
                houses[1].add((r_x, r_y))

    print(len(houses[0] | houses[1]))