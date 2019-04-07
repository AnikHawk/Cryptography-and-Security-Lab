from pymd5 import md5, padding
from Crypto.Hash import SHA256, MD5

msg1 = "d131dd02c5e6eec4693d9a0698aff95c 2fcab58712467eab4004583eb8fb7f89\
55ad340609\
f4b30283e488832571415a 085125e8f7cdc99fd91dbdf280373c5b\
d8823e3156348f5bae6dacd436c919c6 dd53e2b487da03fd02396306d248cda0\
e99f33420f577ee8ce54b67080a80d1e c69821bcb6a8839396f9652b6ff72a70".replace(' ','')

msg2 = "d131dd02c5e6eec4693d9a0698aff95c 2fcab50712467e\
ab4004583eb8fb7f89\
55ad340609f4b30283e4888325f1415a 085125e8f7cdc99fd91dbd7280373c5b\
d8823e3156348f5bae6dacd436c919c6 dd53e23487da03fd02396306d248cda0\
e99f33420f577ee8ce54b67080280d1e c69821bcb6a8839396f965ab6ff72a70".replace(' ','')


h1_md5 = md5(msg1.decode('hex'))
h2_md5 = md5(msg2.decode('hex'))

h1_SHA256 = SHA256.new(msg1.decode('hex'))
h2_SHA256 = SHA256.new(msg2.decode('hex'))

print(h1_md5.hexdigest())
print(h2_md5.hexdigest())
print
print(h1_SHA256.hexdigest())
print(h2_SHA256.hexdigest())
