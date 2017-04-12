import random

out = open('testout.txt','w+')


for i in range(1,1_000_000_000):
    out.write(chr(random.randint(1,127)))

