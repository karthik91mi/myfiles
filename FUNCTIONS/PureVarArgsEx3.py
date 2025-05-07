#Program for demonstrating Variable Arguments
#PureVarArgsEx3.py
def findsum(sno,sname, *vals, city="HYD"):
	print("="*50)
	print("Student ID:{}".format(sno))
	print("Student Name:{}".format(sname))
	print("Living City:{}".format(city))
	s=0
	for val in vals:
		print("\t{}".format(val))
		s=s+val
	print("="*50)
	print("Sum={}".format(s))
	print("="*50)


#main program
findsum(100,"Rossum",10,20,30,40,50) # Function call-1
findsum(200,"Travis",10,20,30,40) # Function call-2
findsum(300,"Kinney",10,20,30) # Function call-3
findsum(400,"Dennis",10,20) # Function call-4
findsum(500,"Kernigan",10) # Function call-5
findsum(600,"KVR") # Function call-6


