from struct import unpack

from . import ByteStream



class Reader(ByteStream):
    def __init__(self, io: bytes, endian: str = "<"):
        super().__init__(io)
        self.endian = endian
    
    def read_int8(self):
        return unpack("b", self.read(1))[0]
    
    def read_uint8(self):
        return unpack("B", self.read(1))[0]
    
    def read_int16(self):
        return unpack(self.endian + "h", self.read(2))[0]
    
    def read_uint16(self):
        return unpack(self.endian + "H", self.read(2))[0]
    
    def read_int32(self):
        return unpack(self.endian + "i", self.read(4))[0]
    
    def read_uint32(self):
        return unpack(self.endian + "I", self.read(4))[0]
    
    def read_int64(self):
        return unpack(self.endian + "q", self.read(8))[0]
    
    def read_uint64(self):
        return unpack(self.endian + "Q", self.read(8))[0]
    
    def read_float32(self):
        return unpack(self.endian + "f", self.read(4))[0]
    
    def read_float64(self):
        return unpack(self.endian + "d", self.read(8))[0]
    
    def read_float16(self):
        return unpack(self.endian + "e", self.read(2))[0]
    
    def read_bool(self):
        return bool(self.read_uint8())
    
    def read_string(self):
        result = ""
        while True:
            symbol = self.read(1)
            
            if symbol == b"\0":
                return result
            
            result += symbol.decode()
    
    readByte = readChar = readInt8 = read_char = read_byte = read_int8
    readUByte = readUChar = readUInt8 = read_uchar = read_ubyte = read_uint8
    
    readShort = readInt16 = read_short = read_int16
    readUShort = readWord = readUInt16 = read_ushort = read_word = read_uint16
    
    readInt = readLong = readInt32 = read_int = read_long = read_int32
    readUInt = readULong = readDWord = readUInt32 = read_uint = read_ulong = read_dword = read_uint32
    
    readQuad = readInt64 = read_quad = read_int64
    readUQuad = readQWord = readUInt64 = read_uquad = read_qword = read_uint64
    
    readFloat = readFloat32 = read_float = read_float32
    readDouble = readFloat64 = read_double = read_float64
    readHalf = readFloat16 = read_half = read_float16
    
    readBool = read_bool
    
    readString = read_string
