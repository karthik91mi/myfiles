#program for deciding whether the given number is +ve or -ve or Zero
#PosNegZeroIfEx.py
n=float(input("Enter a Number:"))
if(n>0):
    print("{} is +VE".format(n))
if(n<0):
    print("{} is -VE".format(n))
if(n==0):
    print("{} is ZERO ".format(n))
print("Program execution Completed")