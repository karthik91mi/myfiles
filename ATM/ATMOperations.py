#ATMOperations.py
from ATMExceptions import DepositError,WithDrawError,InSuffFundError
bal=500.00 # Global Varaible
def  deposit():
	damt=float(input("Enter Ur Deposit Amount:")) # PVM Implicitly Raises ValueError 
	if(damt<=0):
		raise DepositError
	else:
		global bal
		bal=bal+damt
		print("Ur Account xxxxxxxx123 Credited with INR:{}".format(damt))
		print("After Deposit Ur Account xxxxxxxx123  Bal INR:{}".format(bal))

def  withdraw():
	global bal
	wamt=float(input("Enter Ur WithDraw Amount:")) # PVM Implicitly Raises ValueError 
	if(wamt<=0):
		raise WithDrawError
	elif((wamt+500)>bal):
		raise InSuffFundError
	else:
		bal=bal-wamt
		print("Ur Account xxxxxxxx123 Debited with INR:{}".format(wamt))
		print("After With Ur Account xxxxxxxx123  Bal INR:{}".format(bal))

def  balenq():
	print("\t Ur Account xxxxxxxx123  Bal INR:{}".format(bal))
