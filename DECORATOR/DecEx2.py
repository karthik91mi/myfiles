#Program for demoinstrating non-decorator example
#DecEx2.py
def square(kvr):
	def operation():
		n=kvr()
		res=n**2
		return res
	return operation

@square
def  getval():   # This Function Defined by KVR
	return int(input("Enter Any Value:"))


#main program
res=getval() # Calling Normal Function
print("Square={}".format(res))