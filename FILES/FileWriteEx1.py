#Program writing the data to the file
with open("vs.data","w") as fp:
    fp.write(str(1000))
    fp.write("Vivek")
    fp.write(str(34.11))
    print("Data Written to the file")

"""
fp.write("Guido van Rossum\n")
    fp.write("FNO:3-4, Hill Side\n")
    fp.write("Python Software Foundation\n")
    fp.write("NL-56\n")
    print("Data Written to the File")
"""