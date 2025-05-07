#Program implementaing all Arithmetic Operations by Using match case
#MatchCaseEx1.py
print("="*50)
print("\tARITHMETIC OPERATIONS")
print("="*50)
print("\t1.Addtion")
print("\t2.Substraction")
print("\t3.Multiplication")
print("\t4.Division")
print("\t5.Floor Division")
print("\t6.Modulo Division")
print("\t7.Exponentiation")
print("\t8.Exit")
print("="*50)
ch=int(input("Enter ur Choice:"))
match(ch):
    case 1:
        print("Enter Two values for Addtion:")
        a,b=int(input()),int(input())
        print("sum({},{})={}".format(a,b,a+b))
    case 2:
        print("Enter Two values for Sub:")
        a, b = int(input()), int(input())
        print("sub({},{})={}".format(a, b, a - b))
    case 3:
        print("Enter Two values for Mul:")
        k,v = int(input()), int(input())
        print("Mul({},{})={}".format(k, v, k*v))
    case 4:
        print("Enter Two values for Div:")
        k, v = int(input()), int(input())
        print("Div({},{})={}".format(k, v, k/v))
    case 5:
        print("Enter Two values for Floor Div:")
        k, v = int(input()), int(input())
        print("Floor Div({},{})={}".format(k, v, k//v))
    case 6:
        print("Enter Two values for Mod Div:")
        k, v = int(input()), int(input())
        print("Mod({},{})={}".format(k, v, k % v))
    case 7:
        k, v = int(input("Enter Base:")), int(input("Enter Power"))
        print("pow({},{})={}".format(k, v, k**v))
    case 8:
        print("Thx for using program")
    case _: # default case block
        print("Ur Selection of Opeartion is wrong-try again")
print("Program exeution Completed")