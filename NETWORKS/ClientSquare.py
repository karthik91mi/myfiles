#Client Program accepts the value from  KBD and get its Square from  Side Program
#ClientSquare.py
import socket #Step-1
#Step-2
s=socket.socket()
s.connect(("localhost",8888))
print("Client Side Program Obtains Connection from Server Side Program")
print("-"*40)
# Step-3
n=input("Enter a Value for getting its Square:") 
s.send(n.encode())
#step-4
res=s.recv(1024).decode()
print("Square({})={}".format(n,res))
print("-"*40)