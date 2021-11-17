# The Encrypted Orchid from Bloodstained: Ritual of the Night

# I figured out that the description of the weapon was in hexadecimal, so that is the first step here.
# Convert the hex string to ascii characters.
# hex_string = '6f20636b6e7077206772646c7a207a776b6a207075707365756c2078726b7674'
# encoded_text = bytes.fromhex(hex_string).decode('utf-8')
encoded_text = 'OTEwNTgyMTYzMzc4OTQxOTUy.YZU7uQ.CG3QweoAChfRrsm8ypOcnt3VsfA'
print(encoded_text)
# At this point the text was what looked to be a cipher and my first thought was the only one I knew, the Caesar Cipher.
# It was not that one so I then had to look up what the encrypted message was, and I found out that is was a Vigenère
# Cipher instead.


def encode(plain_text, key):
    i = -1
    k_i = -1
    cipher_text = '' 
    while i < len(plain_text) - 1:
        i = i + 1
        k_i = k_i + 1
        plain_letter = ord(plain_text[i])
        key_letter = ord(key[k_i % len(key)])
        letter_location = (plain_letter + key_letter) % 95 + 32
        cipher_text = cipher_text + chr(letter_location)
    return cipher_text


def decode(cipher_text, key):
    i = -1
    k_i = -1
    plain_text = ''
    while i < len(cipher_text) - 1:
        i = i + 1
        k_i = k_i + 1
        cipher_letter = ord(cipher_text[i])
        key_letter = ord(key[k_i % len(key)])
        letter_location = (cipher_letter - key_letter + 127) % 95 + 31
        plain_text = plain_text + chr(letter_location)
    return plain_text


# print(decode(encoded_text, 'orchid'))
# print(encode(decode(encoded_text, 'orchid'), 'orchid'))
print(encode(encoded_text, 'bot'))
print(decode(encode(encoded_text, 'bot'), 'bot'))
