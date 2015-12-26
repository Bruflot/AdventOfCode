import re

with open('input.txt', 'r') as f:
    print(sum(int(x) for x in re.findall(r'\-?[0-9]+', f.read())))
