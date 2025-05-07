#tuplecomphensionex1.py
lst=[3,6,12,7,19,25]
sqlist=( val**2   for val in lst )
print("Type of sqlist=",type(sqlist)) # <class 'generator'>
#Type casr generator object into tuple type
tpl=tuple(sqlist)
print("Type of tpl=",type(tpl))
print("Given List=",lst)
print("Square  List=",tpl)

