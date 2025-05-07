#Program writing the data to the file
#FileWriteEx2.py
with open("C:\\HYD\\addr1.data","a") as fp:
    fp.write("Guido van Rossum\n")
    fp.write("FNO:3-4, Hill Side\n")
    fp.write("Python Software Foundation\n")
    fp.write("Nether landas-56\n")
    print("Data Written to the File")