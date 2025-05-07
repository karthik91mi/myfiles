#Program writing the data to the file
#FileWriteEx3.py
x={10:"Python",20:"Java",30:"C",40:"DS"}
with open("authors.data","a") as fp:
    fp.writelines(str(x)+"\n")
    print("Data Written to the file")