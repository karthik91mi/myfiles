#Program demonstarting opening the files
#FileOpenEx9.py
try:
	with open("kvr.data","x+") as fp:
		print("-------------------------------------------------")
		print("File Opened in Write Mode")
		print("-------------------------------------------------")
		print("File Name : ",fp.name)
		print("File Opening Mode:",fp.mode)
		print("Is this File Readable:",fp.readable())
		print("Is this File Writable:",fp.writable())
		print("Is this File closed:",fp.closed)
		print("-------------------------------------------------")
	print("---------------Out of with open() as --------")
	print("Is this File closed:",fp.closed)

except FileExistsError:
	print("File already exist")