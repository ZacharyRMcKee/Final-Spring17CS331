import services.HuffmanTree
import pickle
import services.ByteBitArray


def preprocess(dict):
    array = [(char,weight) for char, weight in dict.items()] # convert dict into a list of (key, value) tuples
    list = []
    for tup in array: # make list of tuples of all items in dict with values > 0 (should never have negative values)
        if tup[1] != 0:
            list.append(tup)
    list = sorted(list,key = lambda tup: tup[1]) # sort list by least to greatest value in [(key,value)] list
    forest = []
    for i in list:
        forest.append(services.HuffmanTree.HuffmanTree(i[1],i[0]))
    
    while(len(forest) > 1): ## TODO: optimize if needed, there is most likely a better way than calling sorted()
        newTree = services.HuffmanTree.HuffmanTree(forest[0].root.weight+forest[1].root.weight,left=forest[0].root,right=forest[1].root)
        forest = forest[2:]
        forest.append(newTree)
        forest = sorted(forest,key= lambda tree: tree.root.weight)
    print("\nHuffman Tree created!")
    return forest[0]
    
 
def encode(dict,content,outfile,tree):
    '''Input should consist of a huffman-encoded dictionary,
    with keys equal to ASCII characters, and values equal to
    their huffman encoding, stored as a string. Second input is
    the contents of the file read in earlier to create the 
    huffman tree. Third output is name of output file.'''
    counter = 7
    buffer = 0
    out = open(outfile,"wb")
    by = bytearray()
    for line in content:
        for char in line:
            # Go from left to right in the byte
            d = dict[char]
            for bit in d:
                if bit == "1":
                    buffer += 1 << counter
                if counter > 0:
                    counter -= 1
                else:
                    by.append(buffer)
                    if len(by) > 15:
                        out.write(by)
                        by = bytearray()
                    counter = 7
                    buffer = 0
                  
    if buffer != 0:
        by.append(buffer)
        buffer = 0
    out.write(by)
    with open("huff.hex","wb") as dout:
        pickle.dump(tree,dout,protocol=pickle.HIGHEST_PROTOCOL)
    
    

def decode(outfile):
    with open("huff.hex","rb") as dout:
        tree = pickle.load(dout)
    #print(tree)
    coded =  open(outfile,"rb")
    bytestream = services.ByteBitArray.ByteBitArray(coded.read())
    output = open("decoded.txt","w")
    i = 0
    try:
        tree.decodeTree(bytestream,output)
    except StopIteration:
        print("We're done!")
    
















    