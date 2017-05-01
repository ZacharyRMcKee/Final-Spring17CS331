import sys
from services import *
from bitarray import bitarray
import re

file = input("Please enter a filename (ex: test1.txt).\n")
dict = hash_input.file_to_dict(file)
a = ByteBitArray.ByteBitArray()
j = 0

tree = huffman.preprocess(dict,)
d = input("TEST")
b = tree.createDictionary()


str = "101"
str = [str[i:i+8] for i in range(0, len(str),3)]
print(str)









print(b)

