import random
import string

# chars = string.whitespace + string.punctuation + string.digits + string.ascii_letters
# string.whitespace includes  so  we don't add space like that
# This includes all the punctuations, then digits, then letters,both lower case and upper

chars = " " + string.punctuation + string.digits + string.ascii_letters

# You can typecast a string to become a list and make it all in one
chars = list(chars)
key = chars.copy()
random.shuffle(key)
# print(f"chars : {chars}")
# print(f"key   : {key}")

# Encryption part
plain_text = input("Enter a message to be encrypted: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original text : {plain_text}")
print(f"Encrypted text : {cipher_text}")

# Decryption part
cipher_text = input("Enter a message to be decrypted: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted text : {cipher_text}")
print(f"Decrypted text : {plain_text}")