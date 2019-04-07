import collections
import string
from nltk.corpus import wordnet
import re

def decrypt(ciphertext, shift):
    plaintext = ''
    for c in ciphertext:
        if c.isalpha():
            ascii = ord(c)
            shifted = ascii - shift
            if shifted < ord('a'):
                shifted += 26
            plaintext += chr(shifted)
        else:
            plaintext += c
    return plaintext

def calculate_acc(text):
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    valid_words = 0
    for word in words:
        if wordnet.synsets(word):
            valid_words += 1
    return float(valid_words) / len(words)




#alphabet = string.ascii_lowercase
letter_count = collections.Counter()
ciphertext = open("caeser_encrypted.txt", "r").read().lower()

for char in ciphertext:
    if char.isalpha():
        letter_count[char] += 1

sorted_alphabet = sorted(letter_count, key=letter_count.get, reverse=True)

print('Please wait while Decryption is in process. This may take a while... \n')

for i in range(5):
    key = ord(sorted_alphabet[i]) - ord('e')
    key = key % 26
    plaintext = decrypt(ciphertext, key)
    #print(plaintext)
    accuracy_score = calculate_acc(plaintext)
    #print(accuracy_score)
    if(accuracy_score > 0.5):
        print('Decrypted Text: \n' + plaintext)
        file = open('caeser_decrypted.txt', 'w')
        file.write(plaintext)
        file.close()




