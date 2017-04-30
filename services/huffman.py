import services.HuffmanTree
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

    
    

































    