class ByteBitArray:
    # example:
    # |FFFF|0F0F|FACE|...
    #    0    1    2
    def __init__(self,size=10*2**20):  # 10 mebibyte chunks by default
        self.val = bytearray(size)
        
    def __iter__(self):
        for byte in self.val:
            for bit in reversed(range(8)): ## TODO: check efficiency forwards and backwards.
                yield (byte >> bit) % 2
    def 
    def __str__(self):
        out = ""
        for byte in self.val:
            for bit in reversed(range(8)): ## TODO: check efficiency forwards and backwards.
            # Note: This print function is not optimized.
                out += str((byte >> bit) % 2)
            out += "|"
        return out

    
