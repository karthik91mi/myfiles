#Program for Converting JSON File data to Dict Object data---json.load()
#FsonFileDataToDictData.py
import json
with open("emp.json","r") as fp:
	dictobj=json.load(fp)
	for k,v in dictobj.items():
		print("\t{}\t{}".format(k,v))
