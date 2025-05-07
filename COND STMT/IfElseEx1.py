#program for accepting whether a given number of +ve or negative or Zero
#IfElseEx1.py
n=int(input("Enter a Number:")) # +ve   or -ve   or zero
if(n>0):
    print("{} is +VE".format(n))
else:
    if(n<0):
        print("{} is -VE".format(n))
    else:
        print("{} is Zero".format(n))
print("Program execution Completed")

