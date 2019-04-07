import sys
def cont_frac(nom, denom):
    ex = []
    q = nom // denom
    rem = nom % denom
    ex.append(q)
    while rem != 0:
        nom, denom = denom, rem
        q = nom // denom
        rem = nom % denom
        ex.append(q)
    return ex


def convergents(e):
    nom = []
    denom = []
    for i in range(len(e)):
        if i == 0:
            ni, di = e[i], 1
        elif i == 1:
            ni, di = e[i]*e[i-1] + 1, e[i]
        else: # i > 1
            ni = e[i]*nom[i-1] + nom[i-2]
            di = e[i]*denom[i-1] + denom[i-2]
        nom.append(ni)
        denom.append(di)
    return nom, denom


def decrypt(c, d, N):
    if d == 0:
        return 1
    elif d%2 == 1:
        return (c * decrypt(c, d - 1, N)) % N
    else:
        ret = decrypt(c, d / 2, N)
        return (ret*ret) % N


c = int(open('4.3_ciphertext.hex', 'r').read(), 16)
e = int(open('4.4_public_key.hex', 'r').read(), 16)
N = int(open('4.5_modulo.hex', 'r').read(), 16)

n, d = convergents(cont_frac(e, N))

sys.setrecursionlimit(2000)
for i in range(len(d)):
    k = n[i]
    if d[i]%2 == 1 and k!=0 and (e*d[i] - 1) % k == 0 :
        print 'decryption key:', d[i]
        print 'plaintext(int):', decrypt(c, d[i], N)