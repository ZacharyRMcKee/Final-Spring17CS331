class HuffmanTree():
    ''' This class is used for creating Huffman Trees from a hash table input. In this case,
    a Python library dict is used for use as a hash table. '''
    
    class Node:
        def __init__(self,weight,char=None,left=None,right=None):
            self.weight = weight # weight of the node. When paired with a character this means the frequency of that character.
            self.char = char # Should be used on leaves only, for non-leaf nodes this should be set to None.
            self.left = left
            self.right = right
        def __str__(self):
            return "(" + repr(self.char) + ", " + str(self.weight) + ")"
        def printTree(self,level,code=""):
            '''Graphically prints out the HuffmanTree.'''
            if self.left is None:
                left = ""
            else:
                left = "\n" + "|" + self.left.printTree(level+1,code + "0")
            if self.right is None:
                right = ""
            else:
                right = "\n" + "|" + self.right.printTree(level+1,code + "1")
            if self.char:
                out = ", " + code
            else:
                out = ""
            parent = str(self)
            return "\t"*(level) + parent + out + left + right
        def traverseTree(self,binary):
            
            if self.char:
                return self.char # should be char?
            else:
                bit = next(binary)
            if bit:
                return self.right.traverseTree(binary)
            else:
                return self.left.traverseTree(binary)
    def __init__(self,weight,char=None,left=None,right=None): # an empty HuffmanTree cannot exist
        self.root = self.Node(weight,char,left,right) # When a tree is created, it is one of a forest of trees that are to be merged.
    
    def setChildren(self,left,right):
        self.root.left = left
        self.root.right = right
    def decodeTree(self,binary,outfile): # TODO: also include a terminator when max character has been reached
        ''' binary must be a 'bit-iterable' data structure, in that iteration of bits must be simulated.
        # This can be accomplished by using bitshifts.
        # ex. 1101 1100 -> 1011 1000 & 1000 0000 returns a True boolean value, -> 0111 0000 & 1000 0000 returns False, etc to iterate through. '''
        iterator = iter(binary)
        output = []
        i = 0

        while(True):
            i += 1
            if i % 1000000 == 0:
                if (i//1000000)%2==1:
                    print("\\",end="\r")
                else:
                    print("/",end="\r")
            outfile.write(self.traverseTree(iterator))
            
    def traverseTree(self,binary):
        '''Used to traverse the tree given a binary stream for decoding.'''
        return self.root.traverseTree(binary)
        
    def __str__(self):
        return self.printTree(0,"")
    def printTree(self,level,code=""):
        '''Graphically prints out the HuffmanTree.'''
        if self.root.left is None:
            left = ""
        else:
            left = "\n" + "|" + self.root.left.printTree(level+1,code + "0")
        if self.root.right is None:
            right = ""
        else:
            right = "\n" + "|" + self.root.right.printTree(level+1,code + "1")
        if self.root.char:
            out = ", " + code
        else:
            out = ""
        parent = str(self.root)
        return "\t"*(level) + parent + out + left + right
        
    def __repr__(self):
        return str(self)
        
        
    def createDictionary(self):
        # implement depth-first search, return a dictionary with keys = characters,
        # and values equal to their binary codes.
        dict = HuffmanTree.dfs(self.root)
        return dict
        
    def dfs(node,code=""):
        ''' 
        Implements a depth-first search of the HuffmanTree, returning a Dictionary
        which can then be used for encoding a text file into Huffman-coded binary.
        '''
        out = {}
        left = {}
        right = {}
        
        if node.left:   # Does there exist a left child node?
            if node.left.char:  # Is it a leaf (Only leaves have chars)?
                left[node.left.char] = code + '0'
            else:
                left = HuffmanTree.dfs(node.left,code + '0')
        if node.right:  # Does there exist a right child node?
            if node.right.char: # Is it a leaf (Only leaves have chars)?
                right[node.right.char] = code + '1'
            else:
                right = HuffmanTree.dfs(node.right,code + '1')
        if left: # Do we have a dictionary generated from the left child?
            out.update(left)
        if right:# Do we have a dictionary generated from the right child?
            out.update(right)
        return out
        
            
        
    
        
        
        
        
        
        
        
        
        
        