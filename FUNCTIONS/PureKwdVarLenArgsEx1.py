#Program for demonstrating  Keyword Variable Length Arguments
#PureKwdVarLenArgsEx1.py

def  disp(  ** k): # here **k is called variable Keyword Length args--whose type is dict
	print("----------------------------------------")
	print(k,type(k))
	print("----------------------------------------")



#main program
disp(c=30,d=40,a=10,b=20) # Function call-1
disp(city1="HYD",city2="BANG",city3="MUM") # Function call-2
disp(id=100,name="ROSSUM",sub="PYTHON",marks=33.33) # Function call-3
