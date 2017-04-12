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