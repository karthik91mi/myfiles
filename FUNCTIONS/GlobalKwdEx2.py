#Program for demonstrating global keyword
#GlobalKwdEx2.py

def update1():
	global a,b;
	a=a+1
	b=b+1


#main program
a=10
b=20 # Here a and b are called global variables
print("In main program before update1()-->a={} and b={}".format(a,b))
update1()
print("In main program before update1()-->a={} and b={}".format(a,b))





