#Program demonstarting opening the files
#FileOpenEx5.py
with open("stud2.data","w") as fp:
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
