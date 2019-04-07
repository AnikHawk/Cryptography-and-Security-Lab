from Crypto.Cipher import AES

key = ""
iv = ""
ciphertext = open("aes_weak_ciphertext.hex","r").read().decode("hex")

for i in range(16):
    iv += chr(0)

for i in range (31):
	key += chr(0)	

# loop to determine the correct key
# for i in range(32):
# 	i = chr(i)
# 	temp_key = key + i
# 	cipher = AES.new(temp_key, AES.MODE_CBC, iv)
# 	plaintext = cipher.decrypt(ciphertext)
# 	print(plaintext)

key = key + chr(30)
hex_key = key.encode('hex')
file = open('Solution03.hex','w')
file.write(hex_key)
file.close()

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)