class HuffmanTree():
    class Node:
        def __init__(self,weight,char=chr(0),left=None,right=None):
            self.weight = weight
            self.char = char
            self.left = left
            self.right = right
    def __init__(self,weight,char,left=None,right=None): # an empty HuffmanTree cannot exist -- it wouldn't make any sense!
        self.root = self.Node(weight,char,left,right)
    
    def setChildren(self,left,right):
        self.left = left
        self.right = right
    def accessChar(self,binary):
        for bit in binary: # binary must be a 'bit-iterable' data structure, in that iteration of bits must be simulated.
						   # This can be accomplished by using bitshifts.
						   # ex. 1101 1100 -> 1011 1000 & 1000 0000 returns a True boolean value, -> 0111 0000 & 1000 0000, etc to iterate through.
			if bit:
				# go right
			else:
				# go left
		
        