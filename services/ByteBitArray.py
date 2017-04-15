class ByteBitArray:
    # example:
    # |FFFF|0F0F|FACE|...
    #    0    1    2
    def __init__(self,arg=10*2**20):  # 10 mebibyte chunks by default
        if type(arg) is int:
            self.val = bytearray(arg)
        elif type(arg) is bytearray: ## TODO: see if this can be done in one memory write instead of two
            self.val = bytearray(len(arg))
            for i in range(len(arg)):
                self.val[i] = arg[i]
        elif type(arg) is bytes:
            self.val = bytearray(len(arg))
            for i in range(len(arg)):
                self.val[i] = arg[i]
            
    def __iter__(self):
        for byte in self.val:
            for bit in reversed(range(8)): ## TODO: done
                yield (byte >> bit) % 2
    def __str__(self):
        out = ""
        for byte in self.val:
            for bit in reversed(range(8)): ## TODO: done
            # Note: This print function is not optimized.
                out += str((byte >> bit) % 2)
            out += "|"
        return out

    def __setitem__(self,idx,byte):
        self.val[idx] = byte
    def __getitem__(self,idx):
        return self.val[idx]
        
    def __delitem__(self,idx):
        self.val[idx] = 0 # Cannot delete bytes, only set them to zero
