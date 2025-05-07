#StudPickEx1.py-----Program-A
import pickle
def saverecord():
    with open("stud.pick","ab") as fp:
        while(True):
            #read student values from KBD
            print("----------------------------------")
            sno=int(input("Enter Student Number:"))
            sname=input("Enter Student Name:")
            marks=float(input("Enter Student marks:"))
            #create an empty list  and add student values
            l=list()
            l.append(sno)
            l.append(sname)
            l.append(marks)
            #save list object content as a record to the file
            pickle.dump(l,fp)
            print("----------------------------------")
            print("Student Data Saved as Record:")
            print("----------------------------------")
            ch=input("Do u want to insert another Record(yes/no):")
            if(ch.lower()=="no"):
                break

#main program
saverecord()



