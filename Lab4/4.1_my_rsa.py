import random
from fractions import gcd
from Crypto.Util.number import isPrime


def modInv(x,mod):
    inv = []
    for y in range(0,mod-1):
        if (x*y) % mod is 1:
            inv.append(y)
    return inv


def isCoprime(a, b):
    return gcd(a, b) == 1


def encrypt(msg, e, N):
    c = msg ** e
    return c % N


def decrypt(cipher, d, N):
    m = cipher ** d
    return m % N


def generateRSA():
    primes = [i for i in range(10,100) if isPrime(i)]
    p = random.choice(primes)
    primes.remove(p)
    q = random.choice(primes)
    #print ("p:" , p , "  q:" , q)

    N = p * q
    phi = (p - 1) * (q - 1)
    #print ("phi:", phi)

    phi_cp = [i for i in range(2, phi - 1) if isCoprime(i, phi)]
    e = random.choice(phi_cp)
    #print ("e:",e)

    e_inv = modInv(e,phi)
    d = random.choice(e_inv)
    # print ("d:",d)
    return e, d, N


msg = random.randint(1, 99)
print "m:",msg
e, d, N = generateRSA()
cipher = encrypt(msg, e, N)
print "c:",cipher
decipher = decrypt(cipher, d, N)
print "d:",decipher

