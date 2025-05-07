#Program demonstarting opening the files
#FileOpenEx4.py
with open("stud1.data","w") as fp:
	print("File Opened in Write Mode")
	print("Type of fp=",type(fp))