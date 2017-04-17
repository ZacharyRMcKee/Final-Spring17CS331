class HuffmanTree():
''' This class is used for creating Huffman Trees from a hash table input. In this case,
    a Python library dict is used for use as a hash table. '''

    class Node:
        def __init__(self,weight,char=None,left=None,right=None):
            self.weight = weight # weight of the node. When paired with a character this means the frequency of that character.
            self.char = char # Should be used on leaves only, for non-leaf nodes this should be set to None.
            self.left = left
            self.right = right
    def __init__(self,weight,char,left=None,right=None): # an empty HuffmanTree cannot exist
        self.root = self.Node(weight,char,left,right) # When a tree is created, it is one of a forest of trees that are to be merged.
    
    def setChildren(self,left,right):
        self.left = left
        self.right = right
    def decodeTree(self,binary): # TODO: also include a terminator when max character has been reached
        ''' binary must be a 'bit-iterable' data structure, in that iteration of bits must be simulated.
        # This can be accomplished by using bitshifts.
        # ex. 1101 1100 -> 1011 1000 & 1000 0000 returns a True boolean value, -> 0111 0000 & 1000 0000 returns False, etc to iterate through. '''
        iterator = iter(binary)
        output = ""
        try:
            while(True):
                output += self.traverseTree(iterator)
            break
        except StopIteration:
        print(output)
                    
    def traverseTree(self,binary):
        if self.root.char:
            return char
        if bit:
            traverseTree(self.right,next(binary))
        else:
            traverseTree(self.left,next(binary))
    