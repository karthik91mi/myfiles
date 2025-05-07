#RandomAccessFile.py
with open("addr1.data","r") as fp:
    print("----------------------------")
    print("Initial Pos of fp=",fp.tell()) # 0
    filedata=fp.read(5)
    print("File Data=",filedata)
    print("Now Pos of fp=", fp.tell())  # 5
    filedata = fp.read(8)
    print("File Data=", filedata)
    print("Now Pos of fp=", fp.tell())  # 13
    print("----------------------------")
    filedata=fp.read()
    print("File Data=", filedata)
    print("Now Pos of fp=", fp.tell())
    print("----------------------------")
    fp.seek(6) # we  reset fp to 6th index
    filedata = fp.read(7)
    print("File Data=", filedata)
    print("Now Pos of fp=", fp.tell())  # 13
    print("----------------------------")
    filedata = fp.read()
    print("File Data=", filedata)



