#Program for addition of two numbers by using Normal and anonymous Functions
#AnonymousFunEx1.py
def   sumop(a,b): # Normal Function
	c=a+b
	return c

addop=lambda k,v:k+v  # anonymous Functions

#main program
print("By using Normal Function:")
print("Types of sumop=",type(sumop)) # <class,'function'>
print("Enter Two Values")
res=sumop(float(input()),float(input()))
print("sum=",res)
print("------------------------------------------------------------------")
print("By using AnonymousFunction:")
print("Types of addop=",type(addop)) # <class,'function'>
print("Enter Two Values")
res1=addop(float(input()),float(input()))
print("sum=",res1)
