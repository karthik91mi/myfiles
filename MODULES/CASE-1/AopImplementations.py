#AopImplementations.py--file name and module name
def addop():
    print("Enter Two values for Addition")
    a,b=int(input()),int(input())
    print("sum({},{})={}".format(a,b,a+b))
def subop():
    print("Enter Two values for Sub")
    a, b = int(input()), int(input())
    print("sub({},{})={}".format(a, b, a - b))
def mulop():
    print("Enter Two values for Mul")
    a, b = int(input()), int(input())
    print("mul({},{})={}".format(a, b, a * b))
def divop():
    print("Enter Two values for Div")
    a, b = int(input()), int(input())
    print("Div({},{})={}".format(a, b, a / b))
def fdivop():
    print("Enter Two values for Floor Div")
    a, b = int(input()), int(input())
    print("Floor Div({},{})={}".format(a, b, a // b))
def modop():
    print("Enter Two values for Modulo Div")
    a, b = int(input()), int(input())
    print("mod({},{})={}".format(a, b, a % b))
def  expop():
    a,b=int(input("Enter Base:")),int(input("Enter Power:"))
    print("pow({},{})={}".format(a,b,a**b))

