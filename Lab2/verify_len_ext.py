from pymd5 import md5, padding
from len_ext_attack import GenerateToken


def verify(key='key', data='data', append='append'):
    init = key + data
    originalHash = md5(init).hexdigest()
    pad = padding(len(key + data) * 8)
    padded = key + data + pad
    appended = padded + append
    appendedHash = md5(appended).hexdigest()

    passLen = len(key)
    passCmdLen = passLen + len(data)
    paddingLen = len(padding(passCmdLen * 8))
    bits = (passCmdLen + paddingLen) * 8
    newToken = GenerateToken(originalHash, append, bits)
    print '\nH(key||data): \n',originalHash
    print 'H(key||data||pad||append): \n', appendedHash
    print 'LEA Generated Hash: \n', newToken

if __name__ == "__main__":
    pass