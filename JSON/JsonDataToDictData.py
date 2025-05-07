#Program for Converting JSON data into Dict Type----json.loads()
#JsonDataToDictData.py
import json
#Take JSON Data
jsondata='{"SID":"100","SNAME":"ROSSUM","MARKS":"34.56","CNAME":"OUCET"} '
print(jsondata,type(jsondata))
#Convert jsondata into dict type data
dictdata=json.loads(jsondata)
print(dictdata,type(dictdata))
print("--------------------------------------")
for k,v in dictdata.items():
	print("\t{}\t{}".format(k,v))
print("--------------------------------------")