#DecEx3.py
def getline():
	line=input("Enter a Line of Text:")
	return line

def  converttoupper(hyd):  # here converttoupper() is called Decorator
	def caseconvert():
		text=hyd()
		res=text.upper()
		return res
	return caseconvert


#Main Program
resstr=converttoupper(getline)  
res=resstr()
print("Upper Case Data=",res)