key = 10
def encrypt():
    msg = input("Message to encrypt: ") # prompts for message
    msg = msg[::-1] # Reverse string
    encode = ""
    for letter in msg:
        encode += str(ord(letter) + key) + " "
    print(encode)

def decrypt():
    msg = input("Message to decrypt: ")  # prompts for message
    list = msg.split(" ") # Convert string to a list e.g. [114, 97, 98 ...]
    decode = ""
    for character in list:
        if character == '': # ignore empty strings
            continue
        else:
            decode += str(chr(int(character) - key))
    decode = decode[::-1]
    print(decode)

while True:
    prompt = input("Would you like to encrypt (e) or decrypt (d) your message? ")
    if prompt == "e":
        encrypt()
    elif prompt == "d":
        decrypt()
    else:
        continue