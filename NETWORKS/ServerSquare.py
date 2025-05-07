#Server Program accepts the value from CLient Side Program and gives its sqaure
#ServerSquare.py
import socket # Step-1
#Step-2
s=socket.socket()
s.bind(("localhost",8888))
s.listen(2) # Step-3
print("Server Side Program is Ready to accept any client side program")
while(True):
	try:
		cs,ca=s.accept() # Step-4
		#Step-5
		csval=float(cs.recv(1024).decode())
		print("Val of Client={}".format(csval))
		res=csval**2
		cs.send(str(res).encode()) #step-6
	except ValueError:
		cs.send("Don't enter alnums,symbols and strs".encode())







