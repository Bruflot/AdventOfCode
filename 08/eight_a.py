import re
regex = (r'(\\\\)', r'(\\x[0-9a-z]{2})', r'(\\")')
char_len = 0

with open('eight_raw.txt', 'r') as f:
    for line in f:
        char = line.strip()
        char_len += len(char)

        for i in regex:
            char = re.sub(i, '1', char)

        char_len -= len(char.strip('"'))

print(char_len)
