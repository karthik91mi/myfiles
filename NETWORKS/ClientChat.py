#ClientChat.py
import socket
while(True):
	s=socket.socket()
	s.connect(("127.0.0.1",8558))
	cspmsg=input("Student-->")
	if(cspmsg.lower()=="bye"):
		s.send(cspmsg.encode())
		break
	else:
		s.send(cspmsg.encode())
		sermsg=s.recv(1024).decode()
		print("KVR-->{}".format(sermsg))

	


