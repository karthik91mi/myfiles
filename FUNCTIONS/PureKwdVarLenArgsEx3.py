#Program for demonstrating  Keyword Variable Length Arguments
#PureKwdVarLenArgsEx3.py
def findtotalmarks(sno,sname,cls,**submarks):
	print("-------------------------------------------------")
	print("\tStudent Number:{}".format(sno))
	print("\tStudent Name:{}".format(sname))
	print("\tStudent Class:{}".format(cls))
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
findtotalmarks(100,"Rajesh","X",Tel=60,Hindi=70,English=67,Maths=60,Science=60,Social=75)
findtotalmarks(200,"Navenn","XII",Maths=73,Physics=58,Chemistry=60)
findtotalmarks(400,"Veersh","BE",OS=60,DBMS=75,CG=55,SET=62)
findtotalmarks(500,"Rossum","Reserch")