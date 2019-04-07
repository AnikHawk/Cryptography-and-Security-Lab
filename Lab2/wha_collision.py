def WHA(inStr):
    Mask = 0x3FFFFFFF
    outHash = 0
    for char in inStr:
        hx = hex(ord(char))
        byte = int(hx, 16)
        intermediate_value = ((byte ^ 0xCC) << 24) | \
                             ((byte ^ 0x33) << 16) | \
                             ((byte ^ 0xAA) << 8) | \
                             (byte ^ 0x55)
        outHash = (outHash & Mask) + (intermediate_value & Mask)
    return outHash


'''
AS ALL POSSIBLE PERMUTATIONS WOULD GIVE THE SAME HASH VALUE AND
THE COMPUTATION TIME WILL BE VERY MUCH HIGH TO GET ALL POSSIBLE 
PERMUTATIONS, I AM JUST USING A SUBSET CONSISTING OF CYCLIC ROTATED STRINGS.

'''


def rotate(str, n):
    return str[n:] + str[:n]


input_string = open('3.2_input_string.txt', 'r').read()
wha = WHA(input_string)
file = open('solution32.txt', 'w')

print('Few strings with the same hash value are given below: \n')
for n in range(len(input_string)):
    temp_str = rotate(input_string, n)
    temp_hash = WHA(temp_str)
    if temp_hash == wha:
        print(temp_str)
        file.write(temp_str + '\n')


