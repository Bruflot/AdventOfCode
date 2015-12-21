wires = dict()
result = dict()

with open('seven_raw.txt', 'r') as f:
    for line in f:
        expr, var = line.split('->')
        wires[var.strip()] = expr.split()

while 'a' not in result:
    for name, key in wires.items():
        if len(key) == 1:
            # 'a': ['lx']
            if key[0].isdigit():
                result[name] = int(key[0])
            elif key[0] in result:
                result[name] = result[key[0]]
        elif len(key) == 2:
            # 'cs': ['NOT', 'cr']
            if key[1] in result:
                result[name] = 65535 - result[key[1]]
        else:
            # 'ce': ['bk', 'LSHIFT', '1']
            if key[0] in result:
                if key[2].isdigit():
                    if key[1] == 'AND':
                        result[name] = result[key[0]] & int(key[2])
                    elif key[1] == 'OR':
                        result[name] = result[key[0]] | int(key[2])
                    elif key[1] == 'LSHIFT':
                        result[name] = result[key[0]] << int(key[2])
                    elif key[1] == 'RSHIFT':
                        result[name] = result[key[0]] >> int(key[2])
                    else:
                        print(key[1])
                elif key[2] in result:
                    if key[1] == 'AND':
                        result[name] = result[key[0]] & result[key[2]]
                    elif key[1] == 'OR':
                        result[name] = result[key[0]] | result[key[2]]
                    elif key[1] == 'LSHIFT':
                        result[name] = result[key[0]] << result[key[2]]
                    elif key[1] == 'RSHIFT':
                        result[name] = result[key[0]] >> result[key[2]]
                    else:
                        print(key[1])
            elif key[0].isdigit():
                if key[2].isdigit():
                    if key[1] == 'AND':
                        result[name] = int(key[0]) & int(key[2])
                    elif key[1] == 'OR':
                        result[name] = int(key[0]) | int(key[2])
                    elif key[1] == 'LSHIFT':
                        result[name] = int(key[0]) << int(key[2])
                    elif key[1] == 'RSHIFT':
                        result[name] = int(key[0]) >> int(key[2])
                    else:
                        print(key[1])
                elif key[2] in result:
                    if key[1] == 'AND':
                        result[name] = int(key[0]) & result[key[2]]
                    elif key[1] == 'OR':
                        result[name] = int(key[0]) | result[key[2]]
                    elif key[1] == 'LSHIFT':
                        result[name] = int(key[0]) << result[key[2]]
                    elif key[1] == 'RSHIFT':
                        result[name] = int(key[0]) >> result[key[2]]
                    else:
                        print(key[1])

print(result['a'])
