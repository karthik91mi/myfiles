#Program for finding Biggest Two Numbers by using anonymous Functions
#AnonymousFunEx2.py
big=lambda a,b: a if a>b else b if b>a else "Both Values Equal"

#main program
print("Enter Two Values:")
a,b=float(input()),float(input())
bv=big(a,b)
print("big({},{})={}".format(a,b,bv))
