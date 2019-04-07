from Crypto.Hash import SHA256


def hex2bin(str):
    i = int(str,16)
    b = format(i,'0256b')
    return b


def hamming(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


input_string = open('3.1_input_string.txt','r').read()
perturbed_string = open('3.1_perturbed_string.txt','r').read()

hash_real = SHA256.new(input_string).hexdigest()
hash_perturbed = SHA256.new(perturbed_string).hexdigest()

bin_real = hex2bin(hash_real)
bin_perturbed = hex2bin(hash_perturbed)

changed_bits = hamming(bin_real,bin_perturbed)
print changed_bits, 'out of', len(bin_real), 'bits changed!'

open('solution31.hex','w').write(hex(changed_bits))
