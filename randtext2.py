import random

out = open('testout4.txt','w+')

# i in kilobyte-blocks
for i in range(1,1000):
    block = []
    outstr = ""
    block = random.sample([x%128 for x in range(10*1024**2)],10*1024**2)
    outstr = ''.join(chr(x) for x in block)
    out.write(outstr)


