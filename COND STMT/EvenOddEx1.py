#EvenOddEx1.py
n=int(input("Enter a Number:"))
if(n<=0):
    print("{} is Invalid Input:".format(n))
else:
    if(n%2==0):
        print("{} is EVEN".format(n))
    else:
        print("{} is ODD".format(n))