import os
from utils import Reader



class Unpacker(Reader):
	def __init__(self):
		super().__init__(b"", '<')

	def unpack(self, file_path: str):
		super().__init__(open(file_path, 'rb').read())

		magic = self.read(4)
		if magic != b"SCP!":
			raise IOError("Bad SCP file!")

		version = self.readInt()
		sha_length = self.readInt()

		files_count = self.readInt()

		info_offset = self.readInt64()
		info_end_offset = self.readInt64()
		info_length = self.readInt64()

		self.readInt64()
		self.readInt64()
		self.readInt64()
		self.readInt64()

		info_sha = b""
		while True:
			byte = self.read(1)
			if byte != b"\x00":
				info_sha += byte
			else:
				break

		info_sha = info_sha[:sha_length * 2]

		self.seek(info_offset)

		files = []
		for x in range(files_count):
			file_hash_length = self.readShort()
			file_name_length = self.readShort()

			file_output_length = self.readInt64()
			file_offset = self.readInt64()
			file_length = self.readInt64()

			file_hash = self.read(file_hash_length * 2)

			file_name = self.readString()
			file_data = self.buffer[file_offset:file_offset + file_length]

			files.append({
				"name": file_name,
				"hash": file_hash,
				"data": file_data
			})

		dir_name = os.path.basename(os.path.splitext(file_path)[0])
		if not os.path.exists(dir_name):
			os.mkdir(dir_name)

		for file in files:
			file_path = dir_name + "/" + file["name"]

			with open(file_path, 'wb') as f:
				f.write(file["data"])
				f.close()

			print("SCP: Saved {} file!".format(file["name"]))
