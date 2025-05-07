#FileCopy.py
srcfile=input("Enter Source File:")
try:
    with open(srcfile,"r") as rp:
        dstfile=input("Enter Destination File:")
        with open(dstfile,"a") as wp:
            srcdata=rp.read() # Reading the data from SRC File
            wp.write(srcdata)# Wrtinh the SRC File Data to dest File
            print("File Copied--Verify")
except FileNotFoundError:
    print("Source File Does not Exist:")

