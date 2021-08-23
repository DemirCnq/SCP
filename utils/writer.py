from struct import pack

from . import ByteStream



class Writer(ByteStream):
    def __init__(self, io: bytes = b"", endian: str = "<"):
        super().__init__(io)
        self.endian = endian
    
    def write_int8(self, value: int):
        self.write(pack("b", value))
    
    def write_uint8(self, value: int):
        self.write(pack("B", value))
    
    def write_int16(self, value: int):
        self.write(pack(self.endian + "h", value))
    
    def write_uint16(self, value: int):
        self.write(pack(self.endian + "H", value))
    
    def write_int32(self, value: int):
        self.write(pack(self.endian + "i", value))
    
    def write_uint32(self, value: int):
        self.write(pack(self.endian + "I", value))
    
    def write_int64(self, value: int):
        self.write(pack(self.endian + "q", value))
    
    def write_uint64(self, value: int):
        self.write(pack(self.endian + "Q", value))
    
    def write_float32(self, value: float):
        self.write(pack(self.endian + "f", value))
    
    def write_float64(self, value: float):
        self.write(pack(self.endian + "d", value))
    
    def write_float16(self, value: float):
        self.write(pack(self.endian + "e", value))
    
    def write_bool(self, value: bool):
        self.write_uint8(int(value))
    
    def write_string(self, string: str):
        for char in string:
            self.write(char.encode())
        self.write(b"\0")
    
    writeByte = writeChar = writeInt8 = write_char = write_byte = write_int8
    writeUByte = writeUChar = writeUInt8 = write_uchar = write_ubyte = write_uint8
    
    writeShort = writeInt16 = write_short = write_int16
    writeUShort = writeWord = writeUInt16 = write_ushort = write_word = write_uint16
    
    writeInt = writeLong = writeInt32 = write_int = write_long = write_int32
    writeUInt = writeULong = writeDWord = writeUInt32 = write_uint = write_ulong = write_dword = write_uint32
    
    writeQuad = writeInt64 = write_quad = write_int64
    writeUQuad = writeQWord = writeUInt64 = write_uquad = write_qword = write_uint64
    
    writeFloat = writeFloat32 = write_float = write_float32
    writeDouble = writeFloat64 = write_double = write_float64
    writeHalf = writeFloat16 = write_half = write_float16
    
    writeBool = write_bool
    
    writeString = write_string
