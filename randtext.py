import random

out = open('testreal.txt','w+')


for i in range(1,6_400_000):
    out.write(chr(random.randint(1,127)))

