from Crypto.Cipher import AES

key = open("aes_key.hex","r").read().decode('hex')
iv = open("aes_iv.hex","r").read().decode('hex')
ciphertext = open("aes_ciphertext.hex","r").read().decode('hex')

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)


file = open('Solution02.txt','w')
file.write(plaintext)
file.close()
print(plaintext)
