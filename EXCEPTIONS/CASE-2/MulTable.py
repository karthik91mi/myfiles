#Program for MulTable by hitting exceptions
#MulTable.py---File Name and Module Name
from MulExceptions import ZeroError,NegNumError
def  multable(n):
	if(n==0):
		raise ZeroError  # Hitting the exception
	elif(n<0):
		raise NegNumError # Hitting the exception
	elif(n>0):
		print("-----------------------------------------------------")
		print("Mul Table for :{}".format(n))
		print("-----------------------------------------------------")
		for i in range(1,11):
			print("\t{} x {} = {}".format(n,i,n*i))
		print("-----------------------------------------------------")