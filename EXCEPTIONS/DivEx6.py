#Program for accepting Two Numerical Values from KBD and Find their Div
#DivEx6.py---2023-May--KVR Developed This program with 2 Exceptions
#2025---there is chance of Modifying the code by adding some new statements by NEW PROGRAMMER
try:
	print("I am in try block")
	s1=input("Enter First Value:")
	s2=input("Enter Second Value:")
	a=int(s1) # exception generated statement--problemtaic statement
	b=int(s2) # exception generated statement--problemtaic statement
	c=a/b      # exception generated statement--problemtaic statement
	#s="PYTHON" # 2025 adding
	#print(s[11])
except ZeroDivisionError:
	print("Don't enter Zero for Den...")
except ValueError:
	print("Don't Enter Alnums,Strs and symbols")
except : # default except block--last
	print("OOOPS..Some Thing went Wrong")
else:
	print("-------------------------------")
	print("Div={}".format(c))
	print("-------------------------------")
finally:
	print("I am from finally block")