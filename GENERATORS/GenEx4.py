#GenEx4.py
def  kvrrange(Begin,End,Step):
	while(Begin<=End):
		yield Begin
		Begin+=Step # here += is called Short Hand Operator


#main program
g=kvrrange(10,20,2) # here 'g' is an object of <class,'generator'>
print("Content of g=",g)
print("------------------------------------------------")
while(True):
	try:
		print(next(g))
	except StopIteration:
		print("------------------------------------------------")
		break
print("=====================================")
g1=kvrrange(1000,1050,10) # here 'g1' is an object of <class,'generator'>
print("------------------------------------------------")
while(True):
	try:
		print(next(g1))
	except StopIteration:
		print("------------------------------------------------")
		break