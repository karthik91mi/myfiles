#GenEx1.py
def  kvrrange(Val):
	i=0
	while(i<Val):
		yield i
		i=i+1


#main program
g=kvrrange(5) # here 'g' is an object of <class,'generator'>
print("Content of g=",g)
print("------------------------------------------------")
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#print(next(g))----This statement generates StopIteration bcoz generates yielded all the demanded values
