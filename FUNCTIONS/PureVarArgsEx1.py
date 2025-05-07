#Program for demonstrating Variable Arguments
#PureVarArgsEx1.py
def  disp( *k ):  # *param is called Variable Length parameter- whose type is tuple
	print("-"*50)
	print("Number of Values:{}".format(len(k)))
	for v in k:
		print("{}".format(v),end="  ")
	print()
	print("-"*50)


#main program
disp(10,20,30,40) # Function Call-1
disp(10,20,30) # Function Call-2
disp(10,20) # Function Call-3
disp(10) # Function Call-4
disp() # Function call-5
disp(10,"Rakesh",45.67,True,2+3j)