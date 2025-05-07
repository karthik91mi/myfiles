#Program for demonstrating  Keyword Variable Length Arguments
#PureKwdVarLenArgsEx5.py
def findtotalmarks(sno,sname,cls,*vals,state="TS",**submarks):
	print("================================")
	print("Variable Length Values")
	for val in vals:
		print("\t\t{}".format(val))
	print("================================")
	print("-------------------------------------------------")
	print("\tStudent Number:{}".format(sno))
	print("\tStudent Name:{}".format(sname))
	print("\tStudent Class:{}".format(cls))
	print("\tStudent State:{}".format(state))
	print("-------------------------------------------------")
	tm=0
	print("\tSubject\t\tMarks")
	print("-------------------------------------------------")
	for sn,sm in submarks.items():
		print(" \t{}\t\t{}".format(sn,sm))
		tm=tm+sm
	print("-------------------------------------------------")
	print("\tTOTAL MARKS:{}".format(tm))
	print("-------------------------------------------------")

#main program
findtotalmarks(100,"Rajesh","X",1,2,3,4,5,Tel=60,Hindi=70,English=67,Maths=60,Science=60,Social=75)
findtotalmarks(200,"Navenn","XII",10,20,30,40,Maths=73,Physics=58,Chemistry=60)
findtotalmarks(400,"Veersh","BE",100,200,OS=60,DBMS=75,CG=55,SET=62,state="MUM")
findtotalmarks(500,"Rossum","Reserch",-1,-2,-3,-4,-5,state="NL")
findtotalmarks(600,"KVR","Trainer")