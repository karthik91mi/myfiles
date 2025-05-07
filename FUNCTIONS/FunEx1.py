#this program computes Sum of Two Numbers by using functions
#FunEx1.py
def addop(a,b):
    print("i am inside of addop()")
    c=a+b
    return c
#main program
print("Line:8: I am here after Function definition:")
res=addop(3,4) # Function call
print("Line-10--Sum=",res)
res=addop(100,200) # Function call
print("sum=",res)