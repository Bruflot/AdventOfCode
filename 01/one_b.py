def one_b():
    i = 0

    with open('day_one.txt', 'r') as f:
        for index, char in enumerate(f.read()):
            if char is '(':
                i += 1
            elif char is ')':
                i -= 1
            if index == -1:
                break

    print(i)