def two_a():
    total = 0

    with open('day_two.txt', 'r') as f:
        for line in f:
            l, w, h = map(int, line.split('x'))
            rest = min([l*w, w*h, h*l], key=int)
            total += 2*(l*w + w*h + h*l) + rest

    print(total)
