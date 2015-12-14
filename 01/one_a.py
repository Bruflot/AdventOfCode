def one_a():
    i = 0

    with open('one_raw.txt', 'r') as f:
        for char in f.read():
            if char is '(':
                i += 1
            elif char is ')':
                i -= 1

    print(i)