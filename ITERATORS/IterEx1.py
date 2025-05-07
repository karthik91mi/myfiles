#IterEx1.py
lst=[10,20,30,40,50,60,70,80,90] # here lst is one of the Iterable object
#Convert Iterable object into Iterator object by using iter(Iterable object)
lstiter=iter(lst)
print("-----------------------------------------------------------")
print("Type of lst=",type(lst)) # <class,list>
print("Type of lstiter=",type(lstiter)) #<class, list_iterator>
print("-----------------------------------------------------------")
print(next(lstiter))
print(next(lstiter))
print(next(lstiter))
while(True):
	try:
		print(next(lstiter))
	except StopIteration:
		print("-----------------------------------------------------------")
		break

