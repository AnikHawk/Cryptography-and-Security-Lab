
key = open('sub_key.txt', 'r').read()
ciphertext = open('sub_ciphertext.txt', 'r').read()

plaintext = ""
for i in ciphertext:
	if i.isalpha():
		index = (key.find(i))
		plaintext += chr(65 + index)
	else:
		plaintext += i

file = open('Solution01.txt','w')
file.write(plaintext)
file.close()
print(plaintext)
