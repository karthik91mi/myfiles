#DynamicWriteEx1.py
with open("Hyd.info","a") as fp:
    print("Enter Ur data from Key Board press @ to stop: ")
    while(True):
        kbddata=input()
        if(kbddata!="@"):
            fp.write(kbddata+"\n")
        else:
            break
    print("Data written to the file")



