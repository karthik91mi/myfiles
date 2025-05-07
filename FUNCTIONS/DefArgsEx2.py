#Program for Demonstarting the concept of default Arguments.
#DefArgsEx2.py
def  dispstudinfo(sno,sname,marks,crs="PYTHON"):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))


#main program
print("="*50)
print("\tSNO\tNAME\tMARKS\tCOURSE")
print("="*50)
dispstudinfo(100,"RS",34.56) # Function Call
dispstudinfo(200,"TR",44.55) # Function Call
dispstudinfo(300,"DR",14.55) # Function Call
dispstudinfo(400,"KV",11.11) # Function Call
dispstudinfo(500,"TRUMP",10.11) # Function Call
dispstudinfo(600,"BIDEN",30.11,"POLITICS") # Function Call
dispstudinfo(700,"VIVEK",40.11) # Function Call
print("="*50)