#Program for Demonstarting the concept of default Arguments.
#DefArgsEx4.py
def  dispstudinfo1(sno,sname,marks,crs="PYTHON"):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))


def  dispstudinfo2(sno,sname,marks,crs="JAVA"):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

#main program
print("="*50)
print("\tSNO\tNAME\tMARKS\tCOURSE")
print("="*50)
dispstudinfo1(100,"RS",34.56) # Function Call
dispstudinfo1(200,"TR",44.55) # Function Call
dispstudinfo1(300,"DR",14.55) # Function Call
dispstudinfo1(400,"KV",11.11) # Function Call
print("="*50)
print("\tSNO\tNAME\tMARKS\tCOURSE")
print("="*50)
dispstudinfo2(500,"TRUMP",10.11) # Function Call
dispstudinfo2(600,"BIDEN",30.11) # Function Call
dispstudinfo2(700,"VIVEK",40.11) # Function Call
print("="*50)