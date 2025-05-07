#program for demonstrating globals()
#GlobalsFunEx3.py
a=10
b=20
 # here a,b are called global variables
def operations():
	dictobj=globals()
	print("Both  Programmer and Implicit Global variables:")
	for gvn,gvv in dictobj.items():
		print("\t{}-->{}".format(gvn,gvv))
	print("-----------------------------------------------------------------------")
	print("Programmer-Defined Global variables-way1")
	print("Val of a:", dictobj['a'])
	print("Val of b:", dictobj['b'])
	print("-----------------------------------------------------------------------")
	print("Programmer-Defined Global variables-way2")
	print("Val of a:", dictobj.get('a'))
	print("Val of b:", dictobj.get('b'))
	print("-----------------------------------------------------------------------")
	print("Programmer-Defined Global variables-way3")
	print("Val of a:", globals().get('a'))
	print("Val of b:", globals().get('b'))
	print("-----------------------------------------------------------------------")
	print("Programmer-Defined Global variables-way4")
	print("Val of a:", globals()['a'])
	print("Val of b:", globals()['b'])
	print("-----------------------------------------------------------------------")


#main program
operations()


