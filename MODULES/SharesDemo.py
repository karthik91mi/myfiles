#SharesDemo.py
import Shares,time,importlib
def  dispshares(d):
	print("-------------------------------------------")
	print("\tShareName\tShareValue")
	print("-------------------------------------------")
	for sn,sv in d.items():
		print("\t{}\t\t{}".format(sn,sv))
	print("-------------------------------------------")

#main program
d=Shares.sharesinfo()
dispshares(d)
print("I am going to Sleep for 20 seconds")
time.sleep(20)
print("I am coming out of Sleep ")
#reload the module
importlib.reload(Shares)
d=Shares.sharesinfo()
dispshares(d)
print("I am going to Sleep for 20 seconds")
time.sleep(20)
print("I am coming out of Sleep ")
#reload the module
importlib.reload(Shares)
d=Shares.sharesinfo()
dispshares(d)