#ReadValuesEx1.py
lst=[] # empty list
n=int(input("Enter How many value u want in list:"))
if(n<=0):
	print("{} invalid input".format(n))
else:
	for i in range(1,n+1):
		val=float(input("Enter {} Value:".format(i)))
		lst.append(val)
	else:
		print("List of Values:{}".format(lst))