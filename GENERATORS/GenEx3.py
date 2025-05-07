#GenEx3.py
def  kvrrange(Begin,End):
	while(Begin<=End):
		yield Begin
		Begin+=1 # here += is called Short Hand Operator


#main program
g=kvrrange(10,20) # here 'g' is an object of <class,'generator'>
print("Content of g=",g)
print("------------------------------------------------")
while(True):
	try:
		print(next(g))
	except StopIteration:
		print("------------------------------------------------")
		break
print("=====================================")
g1=kvrrange(100,120) # here 'g1' is an object of <class,'generator'>
print("------------------------------------------------")
while(True):
	try:
		print(next(g1))
	except StopIteration:
		print("------------------------------------------------")
		break