#Program for Demonstarting the concept of default Arguments.
#DefArgsEx3.py
def  dispstudinfo(sno,sname,marks,crs="PYTHON",cnt="INDIA"):
	print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))

#main program
print("="*50)
print("\tSNO\tNAME\tMARKS\tCOURSE\tCOUNTRY")
print("="*50)
dispstudinfo(100,"RS",34.56) # Function Call
dispstudinfo(200,"TR",44.55) # Function Call
dispstudinfo(300,"DR",14.55) # Function Call
dispstudinfo(400,"KV",11.11) # Function Call
dispstudinfo(500,"TRUMP",10.11,cnt="USA") # Function Call
dispstudinfo(600,"BIDEN",30.11,"POLITICS","USA") # Function Call
dispstudinfo(700,"VIVEK",40.11) # Function Call
print("="*50)