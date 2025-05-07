#Program for Demonstrating Keyword Arguments
#KeyWordArgsEx2.py
def  dispstudinfo(sno,sname,marks,crs="PYTHON"):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))



#main program
print("="*50)
print("\tSNO\tNAME\tMARKS\tCOURSE")
print("="*50)
dispstudinfo(100,"Monica",66.66) # Function call with Poss Args
dispstudinfo(marks=65.66,sno=200,sname="Sushma")# Function call with Keyword Args
dispstudinfo(crs="Java",sno=300,sname="sangita",marks=55.55)# Function call with Keyword Args
dispstudinfo(sname="Prajwala",marks=66.77,crs="Dsc",sno=400)# Function call with Keyword Args
dispstudinfo(500,"Udaya",crs="Java",marks=22.22)# Function call with Poss args and Keyword Args
print("="*50)

