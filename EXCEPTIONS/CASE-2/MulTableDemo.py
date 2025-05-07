#Program for obtaining MulTable and Handling the exception
#MulTableDemo.py
from MulTable import multable
from MulExceptions import ZeroError,NegNumError
try:
	n=int(input("Enter a Number for Generating Mul table:"))
	multable(n) # Funcrtion call with Result and Exceptions
except ZeroError:
	print("Don't enter Zero for Mul Table:")
except NegNumError:
	print("Don't Enter -ve Number for Mul table:")
except ValueError:
	print("Don't enter alnums,strs and special symbols")