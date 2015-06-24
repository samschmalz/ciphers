#takes user input for the message and the key
message = raw_input("Enter a message: ").lower()
key = raw_input("Enter a single-word key: ").lower()

#turns letters in words into numeric values
def toArray(value):
    arr = []
    for x in range(len(value)):
        item = ord(value[x]) - 97
        arr.append(item)
    return arr

msg = toArray(message)
ky = toArray(key)

#defines the encryption method
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

#defines the decryption method
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

#converts numeric values back into letters
def toLetters(mess):
    final = ""
    for x in mess:
        x += 97
        final += chr(x)
    return final

#gives users the chance to choose to encrypt or decrypt
coded = None
option = raw_input("(e)ncrypt or (d)ecrypt: ")
if option == "e":
    coded = encrypt(msg, ky)
elif option == "d":
    coded = decrypt(msg, ky)

print toLetters(coded)
