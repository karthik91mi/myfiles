#Program for Demonstarting the concept of default Arguments.
#DefArgsEx5.py
def circleareaperi(r,PI=3.14):
	ac=PI*r**2
	pc=2*PI*r
	print("Radius:{}".format(r))
	print("Area of Circle:{}".format(ac))
	print("Peri of Circle:{}".format(pc))


#main program
circleareaperi(float(input("Enter Radius:")))
