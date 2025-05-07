#Function for cal factorial of a number
#FactEx1.py
def factcal(n):
    if(n<0):
        return "{} Is -VE and  No  Factorial".format(n)
    else:
        f=1
        for i in range(1,n+1):
            f=f*i
        return f

#main program
n=int(input("Enter a Number for cal factorial:"))
result=factcal(n)
print("Fact({})={}".format(n,result))