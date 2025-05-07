#Program demonstarting opening the files
#FileOpenEx1.py
try:
	kvr=open("stud.data")
except FileNotFoundError:
	print("File does not exist")
else:
	print("\nType of kvr=",type(kvr))
	print("File Opened in Read Mode Sucessfully")