#Handling the exception by zero is denominater--main program
#DivDemo.py
from Division import divop
from Hyd import HydDivisionError
a=int(input("Enter First Value:"))
b=int(input("Enter Second Value:"))
try:
	res=divop(a,b) # Function call with result or exception
except HydDivisionError:
	print("DON'T ENTER ZERO FOR DEN...")
else:
	print("Div:{}".format(res))
