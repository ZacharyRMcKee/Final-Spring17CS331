import sys
from services import *
from bitarray import bitarray

file = input("Please enter a filename (ex: test1.txt).\n")
dict = hash_input.file_to_dict(file)
huffman.preprocess(dict)
a = bitarray(32)
print(a)