#Prime.py----File Name and Module Name
def  decideprime(n):
	if(n<=1):
		print("{} is invalid".format(n))
	else:
		res="PRIME"
		for i in range(2,n):
			if(n%i==0):
				res="NOT PRIME"
				break
		if(res=="PRIME"):
			print("{} is {}".format(n,res))
		else:
			print("{} is {}".format(n,res))
