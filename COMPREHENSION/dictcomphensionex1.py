#dictcomphensionex1.py
lst=[3,6,12,7,19,25]
sqlist=dict([ (val,val**2)   for val in lst ])
print("Type of sqlist=",type(sqlist))
for n,s in sqlist.items():
	print("\t{}-->{}".format(n,s))

