vowels = ('a', 'e', 'i', 'o', 'u')
bad_strings = ('ab', 'cd', 'pq', 'xy')
nice = 0

with open('five_raw.txt', 'r') as f:
    for line in f:
        if sum(line.count(v) for v in vowels) < 3:
            continue

        if any(word in line for word in bad_strings):
            continue

        for index, char in enumerate(line):
            if index+1 < len(line):
                if line[index+1] is char:
                    nice += 1
                    break


print(nice)
