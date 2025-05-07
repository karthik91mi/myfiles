#Generating  Exception when division by zero by using raise kwd
#Division.py--File Name and Module Name
from Hyd import  HydDivisionError
def  divop(a,b):
	if(b==0):
		raise HydDivisionError # raise kwd is used for Hitting / generating the exception
	else:
		return (a/b)