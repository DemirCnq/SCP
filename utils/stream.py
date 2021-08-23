class ByteStream:
    def __init__(self, io: bytes):
        self.buffer = io
        self.offset = 0
    
    def read(self, length: int):
        data = self.buffer[self.offset:self.offset + length]
        self.offset += length
        
        return data
    
    def write(self, data: bytes):
        self.buffer += data
    
    def fill(self, length: int):
        self.buffer += b"\0" * length
    
    def seek(self, position: int):
        self.offset = position
    
    def skip(self, amount: int):
        self.offset += amount
    
    def awaible(self, size: int = 0):
        return len(self.buffer[self.offset:]) >= size
    
    def tell(self):
        return self.offset
