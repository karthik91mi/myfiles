#listcomphensionex2.py
lst=[3,6,-12,7,-19,25,-56,23,-78,89,0,12]
pslist=[  val  for val in lst  if val>0]	
nglist=[ val for val in lst if val<0]
print("Given List=",lst)
print("List of +ve Elements=",pslist)
print("List of -ve Elements=",nglist)
