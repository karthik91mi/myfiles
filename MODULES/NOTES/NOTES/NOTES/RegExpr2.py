#RegExpr2.py
import re
gd="Python is an oop Lang.Python is also Fun Prog Lang"
sp="hyd"
res=re.search(sp,gd)  # here res is an object of re.Match class OR NoneType
if(res!=None):
	print("Search is Successful")
	print("Start Index:{}".format(res.start()))
	print("End Index:{}".format(res.end()))
	print("Value:{}".format(res.group()))
else:
	print("Search is Un-Successful")

