from Crypto.PublicKey import RSA

key = open("key", "r").read()
keypub = open("key.pub", "r").read()
privateKey = RSA.importKey(key)
publicKey = RSA.importKey(keypub)

msg = "hello world"
cipher = publicKey.encrypt(msg, "")[0]
print(cipher.encode("hex"))
plain = privateKey.decrypt(cipher)
print(plain)