#ATMMainProg.py
from ATMMenu import menu
from ATMExceptions import DepositError,WithDrawError,InSuffFundError
from ATMOperations import deposit,withdraw,balenq
while(True):
	menu()
	ch=int(input("\t\tEnter Ur Choice:"))
	match(ch):
		case 1:
			try:
				deposit()
			except ValueError:
				print("Don't try deposit Alnums,strs and Special Symbols")
			except DepositError:
				print("Don't try deposit Zero / -Ve Values")
		case 2:
			try:
				withdraw()
			except ValueError:
				print("Don't try Withdraw Alnums,strs and Special Symbols")
			except WithDrawError:
				print("Don't try withdraw Zero / -Ve Values")
			except InSuffFundError:
				print("Ur Account does not have suff funds--read python notes")
		case 3:
			balenq()
		case 4:
			print("Thx for this program")
			break
		case _:
			print("Ur Selection of Operation is Wrong--Try again")