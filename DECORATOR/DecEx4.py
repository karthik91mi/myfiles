#DecEx4.py

def converter(kvr):
	def caseconvert():
		text=kvr()
		res=text.upper()
		return res
	return caseconvert

@converter
def getline():
	line=input("Enter a Line of Text:")
	return line

#main program
res=getline()
print("Upper Case Data:",res)
