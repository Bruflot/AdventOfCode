key = '1113122113'


def output(_in):
    n = 1
    new_str = ''
    for index, char in enumerate(_in):
        if index+1 < len(_in):
            if _in[index+1] == char:
                n += 1
                continue

        new_str += str(n) + char
        n = 1

    return new_str

for i in range(0, 50):
    key = output(key)

print(len(key))
