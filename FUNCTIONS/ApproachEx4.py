##Program for defining a Function for cal Mul of two numbers
#ApproachEx4.py
#INPUT---------->Taking in Function Body
#PROCESS-------->Done in Function Body
#RESULT OR OUTPUT-->Given to Function Call
def  mulop():
    #Input
    a = float(input("Enter First Value:"))
    b = float(input("Enter Second Value:"))
    # Procees
    c = a * b
    #Give the Result to Function call
    return a,b,c

#main program
a,b,res=mulop() # Function call with Multipline assigment
print("mul({},{})={}".format(a,b,res))
print("-------------OR------------------")
res=mulop() #function call with Single Line assignment
#here res is type of tuple
print(res,type(res)) # (7.0, 8.0, 56.0) <class 'tuple'>
print("mul({},{})={}".format(res[-3],res[-2],res[-1]))

