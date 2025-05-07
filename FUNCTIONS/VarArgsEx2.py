#Program for demonstrating Variable Arguments
#VarArgsEx2.py
def disp(a,b,c,d):  # Function Def-1
	print(a,b,c,d)

disp(10,20,30,40) # Function Call-1
#-------------------------------------------------------------------------------------
def disp(a,b,c):   # Function Def-2
	print(a,b,c)

disp(10,20,30) # Function Call-2
#-------------------------------------------------------------------------------------
def disp(a,b):   # Function Def-3
	print(a,b)

disp(10,20) # Function Call-3
#-------------------------------------------------------------------------------------
def disp(a):   # Function Def-4
	print(a)

disp(10) # Function Call-4
