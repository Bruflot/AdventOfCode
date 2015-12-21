import operator

wires = dict()
result = dict()
operators = {
    'AND': operator.and_,
    'OR': operator.or_,
    'LSHIFT': operator.lshift,
    'RSHIFT': operator.rshift
}

with open('seven_raw.txt', 'r') as f:
    for line in f:
        expr, var = line.split('->')
        wires[var.strip()] = expr.split()
    wires['a'] = ['2797']

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
                    result[name] = operators[key[1]](result[key[0]], int(key[2]))
                elif key[2] in result:
                    result[name] = operators[key[1]](result[key[0]], result[key[2]])
            elif key[0].isdigit() and key[2] in result:
                result[name] = operators[key[1]](int(key[0]), result[key[2]])

print(result['a'])
