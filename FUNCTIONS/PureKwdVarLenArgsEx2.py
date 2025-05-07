#Program for demonstrating  Keyword Variable Length Arguments
#PureKwdVarLenArgsEx2.py

def  disp(  ** k): # here **k is called variable Keyword Length args--whose type is dict
	print("----------------------------------------")
	for kv,vv  in k.items():
		print("\t{}-->{}".format(kv,vv))
	print("----------------------------------------")



#main program
disp(c=30,d=40,a=10,b=20) # Function call-1
disp(city1="HYD",city2="BANG",city3="MUM") # Function call-2
disp(id=100,name="ROSSUM",sub="PYTHON",marks=33.33) # Function call-3
disp(sid=123, sname="Mahesh",hobby1="Eating",hobby2="Sleep",hobby3="Cahtting")