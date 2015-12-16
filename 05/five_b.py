nice = 0

with open('five_raw.txt', 'r') as f:
    for line in f:
        check_a, check_b = False, False

        for index, char in enumerate(line):
            if index+1 < len(line):
                temp = char + line[index+1]
                if line.count(temp) >= 2:
                    check_a = True

            if index+2 < len(line):
                if line[index+2] is char:
                    check_b = True

        if check_a and check_b:
            nice += 1

print(nice)
