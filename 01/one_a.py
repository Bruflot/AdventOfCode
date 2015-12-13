def day_one_a():
    i = 0

    with open('day_one.txt', 'r') as f:
        for char in f.read():
            if char is '(':
                i += 1
            elif char is ')':
                i -= 1

    print(i)
