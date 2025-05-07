#CSRT.py---main program
from FigureMenu import menu
from Circle import area as ca,peri as cp
from Square import area as sa,peri as sp
from Rect import area as ra, peri as rp
while(True):
	menu()
	ch=int(input("\tEnter Ur Choice:"))
	if(ch==1):
		ca()
	elif(ch==2):
		cp()
	elif(ch==3):
		sa()
	elif(ch==4):
		sp()
	elif(ch==5):
		ra()
	elif(ch==6):
		rp()
	elif(ch==7):
		print("Student must do")
	elif(ch==8):
		print("Student must do")
	elif(ch==9):
		break
	else:
		print("Ur Selection of Operation is Wrrong")


