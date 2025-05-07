#Program for demonstrating  Keyword Variable Length Arguments
#KwdVarLenArgsEx2.py--This Program will execute
def  disp(a,b,c,d): #Function Def-1
	print("-----------------------------------------------------")
	print(a,b,c,d)
	print("-----------------------------------------------------")

disp(c=30,d=40,a=10,b=20) # Function call-1
#-------------------------------------------------------------------------------
def  disp(x,y,z): #Function Def-2
	print("-----------------------------------------------------")
	print(x,y,z)
	print("-----------------------------------------------------")

disp(x="HYD",y="BANG",z="MUM") # Function call-2
#-------------------------------------------------------------------------------------
def  disp(K,L,M,N): #Function Def-3
	print("-----------------------------------------------------")
	print(K,L,M,N)
	print("-----------------------------------------------------")

disp(K=100,L="ROSSUM",M="PYTHON",N=33.33) # Function call-3
