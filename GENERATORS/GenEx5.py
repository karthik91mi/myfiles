#GenEx5.py
def getcourses():
	yield "PYTHON"
	yield "JAVA"
	yield "DSA"
	yield "DSc"


#main program
crs=getcourses() # here crs is of type <class,'generator'>
print(next(crs))
print(next(crs))
print(next(crs))
print(next(crs))
