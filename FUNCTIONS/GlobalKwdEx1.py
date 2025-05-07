#Program for demonstrating global keyword
#GlobalKwdEx1.py
def incr1():
	global a
	a=a+1

def incr2():
	global a
	a=a*2


#main program
a=10 # global variable
print("Val of a in main program before incr1()=",a)  # 10
incr1()
print("Val of a in main program after incr1()=",a) # 11
incr2()
print("Val of a in main program after incr2()=",a) # 22