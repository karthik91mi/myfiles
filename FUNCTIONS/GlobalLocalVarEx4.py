#Program for demonstrating local and global variables
#GlobalLocalVarEx4.py
def  learnML():
	sub1="ML"
	print("To develop '{}' Programs, we Use '{}' Lang".format(sub1,lang))
	#print(sub2) can't access bcoz sub2 is local in learnDL()

def  learnDL():
	sub2="DL"
	print("To develop '{}' Programs, we Use '{}' Lang".format(sub2,lang))
	#print(sub1) an't access bcoz sub1 is local in learnML()

#main program
#learnML()----here global variable lang can't be accessed in its body bcoz it was defined after its function call
lang="PYTHON" # Global variable
learnDL()
