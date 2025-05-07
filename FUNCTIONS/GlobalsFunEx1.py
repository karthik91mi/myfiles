#program for demonstrating globals()
#GlobalsFunEx1.py
a=10
b=20
c=30
d=40 # here a,b,c, and d are called global variables
def operations():
	x=100
	y=200
	z=300
	k=400  # here x,y,z,k are called Local variables
	res=x+y+z+k+a+b+c+d
	print("Result=",res)

#main program
operations()


