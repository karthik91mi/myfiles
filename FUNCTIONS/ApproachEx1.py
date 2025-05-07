#Program for defining a Function for cal Mul of two numbers
#ApproachEx1.py
#INPUT---------->Taking From Function Call
#PROCESS-------->Done in Function Body
#RESULT OR OUTPUT-->Given to Function Call
def mulop(a,b): # here a ,b are called formal parameters
    c=a*b # here c is called local variable
    return c

#main program
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
res=mulop(a,b) # Function call
print("Mul({},{})={}".format(a,b,res))
