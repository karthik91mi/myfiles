#Program for demonstrating  Keyword Variable Length Arguments
#KwdVarLenArgsEx1.py--This Program will not execute as it is
def  disp(a,b,c,d): #Function Def-1
	print("-----------------------------------------------------")
	print(a,b,c,d)
	print("-----------------------------------------------------")

def  disp(x,y,z): #Function Def-2
	print("-----------------------------------------------------")
	print(x,y,z)
	print("-----------------------------------------------------")

def  disp(K,L,M,N): #Function Def-3
	print("-----------------------------------------------------")
	print(K,L,M,N)
	print("-----------------------------------------------------")

#main program
disp(c=30,d=40,a=10,b=20) # Function call-1
disp(x="HYD",y="BANG",z="MUM") # Function call-2
disp(K=100,L="ROSSUM",M="PYTHON",N=33.33) # Function call-3
