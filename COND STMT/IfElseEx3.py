#program for accepting any digit and print its name
#IfElseEx3.py
n=int(input("Enter a Digit:"))#0 1 2 3 4 5 6 7 8 9
if(n==0):
    print("{} is Zero".format(n))
else:
    if(n==1):
        print("{} is One".format(n))
    else:
        if(n==2):
            print("{} is TWO".format(n))
        else:
            if(n==3):
                print("{} is THREE".format(n))
            else:
                if(n==4):
                    print("{} is FOUR".format(n))
                else:
                    if(n==5):
                        print("{} is FIVE".format(n))
                    else:
                        if(n==6):
                            print("{} is SIX".format(n))
                        else:
                            if(n==7):
                                print("{} is SEVEN".format(n))
                            else:
                                if(n==8):
                                    print("{} is EIGHT".format(n))
                                else:
                                    if(n==9):
                                        print("{} is NINE".format(n))
                                    else:
                                        print("{} is a Number".format(n))
print("Program execution Completed")
