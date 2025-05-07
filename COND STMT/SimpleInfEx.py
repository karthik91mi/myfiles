#program for accepting any digit and print its name
#SimpleIfEx.py
n=int(input("Enter a Digit:"))#0 1 2 3 4 5 6 7 8 9
if(n==0):
    print("{} is Zero".format(n))
if(n==1):
    print("{} is ONE".format(n))
if(n==2):
    print("{} is TWO".format(n))
if(n==3):
    print("{} is THREE".format(n))
if(n==4):
    print("{} is FOUR".format(n))
if(n==5):
    print("{} is FIVE".format(n))
if(n==6):
    print("{} is SIX".format(n))
if(n==7):
    print("{} is SEVEN".format(n))
if(n==8):
    print("{} is EIGHT".format(n))
if(n==9):
    print("{} is NINE".format(n))
if( n in [-1,-2,-3,-4,-5,-6,-7,-8,-9]):
    print("{} is -Ve Digit".format(n))
if( n not in [-1,-2,-3,-4,-5,-6,-7,-8,-9] and n not in [0,1,2,3,4,5,6,7,8,9] ):
    print("{} is NUMBER".format(n))
print("Program execution Completed")