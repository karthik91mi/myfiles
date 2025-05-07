#StudUnPickEx1.py---Program-B
import pickle
try:
    with open("C:\\Users\Kvr\\PycharmProjects\\6pmfiles1\\stud.pick","rb") as fp:
        print("--------------------------")
        while(True):
            try:
                obj=pickle.load(fp)
                for val in obj:
                    print("{}".format(val),end="\t")
                print()
            except EOFError:
                print("--------------------------")
                break
        #Lots of code
except FileNotFoundError:
    print("File does not exist")
