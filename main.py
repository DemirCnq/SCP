import argparse
from scp import Unpacker, Packer



if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Simple Supercell Packs files unpacker/packer")

	parser.add_argument('path', help="Input SCP file", type=str)
	parser.add_argument('-d', '--unpack', help="Unpack files from input SCP file", action="store_true")
	parser.add_argument('-c', '--pack', help="Pack files from folder to input SCP file", action="store_true")

	args = parser.parse_args()

	if args.path:
		file_path = args.path

		if args.unpack:
			unpacker = Unpacker()
			unpacker.unpack(file_path)

		elif args.pack:
			packer = Packer()
			packer.pack(file_path)

		print("Done!")
