import json


def parse(data):
    if type(data) is int:
        return data
    elif type(data) is list:
        return sum(map(parse, data))
    elif type(data) is not dict:
        return 0
    elif 'red' in data.values():
        return 0

    return parse(list(data.values()))

with open('input.txt', 'r') as f:
    print(parse(json.load(f)))
