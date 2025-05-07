#Program for accepting Two Numerical Values from KBD and Find their Div
#DivEx5.py
try:
	print("I am in try block")
	s1=input("Enter First Value:")
	s2=input("Enter Second Value:")
	a=int(s1) # exception generated statement--problemtaic statement
	b=int(s2) # exception generated statement--problemtaic statement
	c=a/b      # exception generated statement--problemtaic statement
except :
	print("ooops....Some Thing went Wrong")
else:
	print("-------------------------------")
	print("Div={}".format(c))
	print("-------------------------------")
finally:
	print("I am from finally block")