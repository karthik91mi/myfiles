#EvenOddEx2.py
n=int(input("Enter a Number:"))
if(n<=0):
    print("{} is Invalid Input:".format(n))
elif(n%2==0):
    print("{} is EVEN".format(n))
elif(n%2!=0):
    print("{} is ODD".format(n))