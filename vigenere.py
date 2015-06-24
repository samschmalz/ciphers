message = raw_input("Enter a message: ").lower()
key = raw_input("Enter a word key: ").lower()

def toArray(value):
    arr = []
    for x in range(len(value)):
        item = ord(value[x]) - 97
        arr.append(item)
    return arr

msg = toArray(message)
ky = toArray(key)

def encrypt(m, k):
    result = []
    spaces = 0
    for x in range(len(m)):
        if m[x] < 0:
            result.append(m[x])
            spaces += 1
        else:
            next = m[x] + k[(x - spaces) % len(k)]
            result.append(next % 26)
    return result

def decrypt(m, k):
    result = []
    spaces = 0
    for x in range(len(m)):
        if m[x] < 0:
            result.append(m[x])
            spaces += 1
        else:
            next = m[x] - k[(x - spaces) % len(k)] + 26
            result.append(next % 26)
    return result

def toLetters(mess):
    final = ""
    for x in mess:
        x += 97
        final += chr(x)
    return final

coded = None
option = raw_input("(e)ncrypt or (d)ecrypt: ")
if option == "e":
    coded = encrypt(msg, ky)
elif option == "d":
    coded = decrypt(msg, ky)

print toLetters(coded)
