#Program for Demonstarting the concept of Possitional Arguments.
#PossArgsEx1.py
def  dispstudinfo(sno,sname,marks):
	print("\t{}\t{}\t{}".format(sno,sname,marks))


#main program
print("="*50)
print("\tSNO\tNAME\tMARKS")
print("="*50)
dispstudinfo(100,"RS",34.56) # Function Call
dispstudinfo(200,"TR",44.55) # Function Call
dispstudinfo(300,"DR",14.55) # Function Call
dispstudinfo(400,"KV",11.11) # Function Call
print("="*50)