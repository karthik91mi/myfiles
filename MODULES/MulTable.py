#MulTable.py--File Name and Module name
def table(n):
	if(n<=0):
		print("{} is invalid input".format(n))
	else:
		print("Mul Table for :{}".format(n))
		for i in range(1,11):
			print("\t{} x {}={}".format(n,i,n*i))
	