import os
import hashlib

from utils import Writer



class Packer(Writer):
	def __init__(self):
		super().__init__()
		self.info_buffer = b""

	def pack(self, directory: str):
		print("Not avaible now...")
		# files = []
		# for file_name in os.listdir(directory):
		# 	file_data = open(directory + "/" + file_name, 'rb').read()
		# 	file_hash = hashlib.md5(file_data).digest()

		# 	files.append({
		# 		"name": file_name,
		# 		"hash": file_hash,
		# 		"data": file_data,
		# 		"offset": len(self.info_buffer)
		# 	})

		# 	self.info_buffer += file_data

		# header_length = 4 + 8 + 4 + 8 * 3 + 8 * 4 + 32 + 1
		# header_length_ = header_length + len(self.info_buffer)

		# self.write(b"SCP!")

		# self.writeInt(1)
		# self.writeInt(16)

		# self.writeInt(len(files))

		# self.writeInt64(header_length_)
		# self.writeInt64(0)
		# self.writeInt64(0)

		# self.writeInt64(0)
		# self.writeInt64(0)
		# self.writeInt64(0)
		# self.writeInt64(0)

		# self.write(b"\xff" * 32 + b"\x00") # info_sha

		# self.write(self.info_buffer)

		# for file in files:
		# 	self.writeShort(len(file["hash"]) // 2)
		# 	self.writeShort(len(file["name"]))

		# 	self.writeInt64(len(file["data"]))
		# 	self.writeInt64(header_length + file["offset"])
		# 	self.writeInt64(len(file["data"]))

		# 	self.write(file["hash"])
		# 	self.writeString(file["name"])

		# pack_name = directory + ".scp"
		# with open(pack_name, 'wb') as scp:
		# 	scp.write(self.buffer)
		# 	scp.close()
