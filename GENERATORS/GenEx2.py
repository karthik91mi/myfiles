#GenEx2.py
def  kvrrange(Val):
	i=0
	while(i<=Val):
		yield i
		i=i+1


#main program
g=kvrrange(10) # here 'g' is an object of <class,'generator'>
print("Content of g=",g)
print("------------------------------------------------")
while(True):
	try:
		print(next(g))
	except StopIteration:
		print("------------------------------------------------")
		break
	
