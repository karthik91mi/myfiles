#Program for demoinstrating non-decorator example
#DecEx1.py
def  getval():   # This Function Defined by KVR
	return int(input("Enter Any Value:"))


def square( kvr ): # Here Square is called Decorator
	def  operation(): # Inner Function will the operations for kvr function (alias name of getval())
		n=kvr()
		res=n**2
		return res
	return operation
	

#main program
result=square(getval)
res=result()
print("Square={}".format(res))
