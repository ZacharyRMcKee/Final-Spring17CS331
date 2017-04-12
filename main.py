import sys
from services import *

file = input("Please enter a filename (ex: test1.txt).\n")
dict = hash_input.file_to_dict(file)
huffman.codify(dict)
