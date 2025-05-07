#ServerChat.py
import socket
s=socket.socket()
s.bind(("127.0.0.1",8558))
s.listen(2)
print("SSP is Ready to accept any CSP Request")
while(True):
	cs,ca=s.accept()
	csmsg=cs.recv(1024).decode()
	print("Student-->{}".format(csmsg))
	sermsg=input("KVR-->")
	cs.send(sermsg.encode())


