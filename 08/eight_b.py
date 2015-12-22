char_len = 0

with open('eight_raw.txt', 'r') as f:
    for line in f:
        char = line.strip()
        char_len -= len(char)
        char = '"' + char.replace('\\', '\\\\').replace('\"', '\\\"') + '"'
        char_len += len(char)

print(char_len)
