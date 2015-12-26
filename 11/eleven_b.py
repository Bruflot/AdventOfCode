abc = 'abcdefghijklmnopqrstuvwxyz'
exclude = 'iol'
password = 'hepxxyzz'

def validate(pword):
    for i in range(0, len(pword)):
        if pword[i:i+3] in abc:
            break
        elif i == len(pword)-3:
            return False

    for char in exclude:
        if char in pword:
            return False

    chars = set()
    for index, char in enumerate(pword):
        if index+1 < len(pword):
            if char is pword[index+1]:
                chars.add(char)

    if len(chars) < 2:
        return False

    return True

def generate(pword):
    n = -1
    pword = list(pword)

    while pword[n] == 'z':
        pword[n] = 'a'
        n -= 1

    pword[n] = chr(ord(pword[n]) + 1)
    return ''.join(pword)


password = generate(password)
while not validate(password):
    password = generate(password)

print(password)
