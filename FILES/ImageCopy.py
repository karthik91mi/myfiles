#ImageCopy.py
try:
    with open("C:\HYD\human.png","rb") as rp:
        with open("programmer.png","wb") as wp:
            srcdata=rp.read() # Reading the data from SRC File
            wp.write(srcdata)# Wrtinh the SRC File Data to dest File
            print("Image File Copied--Verify")
except FileNotFoundError:
    print("Source File Does not Exist:")

