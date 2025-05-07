#Program for demoinstrating non-decorator example
#Non-DecEx1.py
def  getval():   # This Function Defined by KVR
	return int(input("Enter Any Value:"))

def  square():
	n=getval()
	res=n**2
	return res

def  squareroot():
	n=getval()
	res=n**0.5
	return res

def cube():
	n=getval()
	res=n**3
	return res

#Main program
res=square()
print("Square ={}".format(res))
print("------------------------------------------")
res=squareroot()
print("Square Root ={}".format(res))
print("------------------------------------------")
res=cube()
print("Cube ={}".format(res))
