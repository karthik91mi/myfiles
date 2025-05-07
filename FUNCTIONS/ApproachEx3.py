#Program for defining a Function for cal Mul of two numbers
#ApproachEx3.py
#INPUT---------->TTaking From Function Call
#PROCESS-------->Done in Function Body
#RESULT OR OUTPUT-->Displayed in Function Body
def  mulop(k,v):
    r=k*v
    print("mul({},{})={}".format(k,v,r))

#main program
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
mulop(a,b) # Function call

