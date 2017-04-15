from HuffmanTree import *
def codify(dict):
    array = [(key,value) for key, value in dict.items()] # convert dict into a list of (key, value) tuples
    list = []
    for tup in array: # make list of tuples of all items in dict with values > 0 (should never have negative values)
        if tup[1] != 0:
            list.append(tup)
    list = sorted(list,key = lambda tup: tup[1]) # sort list by least to greatest value in [(key,value)] list
    forest = []
    for i in list:
        forest.append(HuffmanTree(i[0],i[1]))
    print(forest)
    
    
    
    

































    