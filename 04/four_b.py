from hashlib import md5

secret = 'iwrupvqb'
i = 0

while True:
    _hash = md5()
    _hash.update(str(secret + str(i)).encode('utf-8'))
    _hex = _hash.hexdigest()
    if _hex[:6] == '000000':
        break
    i += 1

print(i)
