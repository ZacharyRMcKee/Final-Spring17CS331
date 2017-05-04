import sys
from services import *
import re
import time

def hufCode():
    
    filename = input("Please enter a filename (ex: test1.txt).\n")
    start = time.time()
    file = open(filename)
    print("Loading file into RAM.",end='\r')
    filecontents = file.readlines()
    print("\rFile loaded.                \n")

    dict = hash_input.file_to_dict(filecontents)
    a = ByteBitArray.ByteBitArray()
    tree = huffman.preprocess(dict,)
    b = tree.createDictionary()
    print(b)
    print("Encoding file, please wait ...")
    huffman.encode(b,filecontents,"out.hex",tree)
    file.close()
    filecontents = None
    print("Done encoding.")
    huffman.decode("out.hex")
    print("Done decoding.")
    end = time.time()
    print(end - start)

if __name__ == '__main__':
    print("TEST")
    hufCode()



