#program for demonstrating globals()
#GlobalsFunEx2.py
a=10
b=20
c=30
d=40 # here a,b,c, and d are called global variables
def operations():
	a=100
	b=200
	c=300
	d=400  # here a,b,c,d are called Local variables
	res=a+b+c+d+globals()['a']+globals()['b']+globals()['c']+globals()['d']
	print("Result=",res)

#main program
operations()


