#aoppro.py----File Name and Module name
from AopMenu import menu
from AopImplementations import *
def  runaopproj():
	while(True):
		menu()
		ch=int(input("Enter Ur Choice:"))
		match(ch):
			case 1:addop()
			case 2:subop()
			case 3:mulop()
			case 4:divop()
			case 5:fdivop()
			case 6:modop()
			case 7:expop()
			case 8:
				print("Thx for using this program ")
				break
			case _:
				print("Ur Selection of Operations is wrong!!")

