import socket
sk = socket.socket()
sk.connect(("127.0.0.1",8888))
while True :
	send_data = input("your message\n")
	sk.sendall(bytes(send_data,encoding="utf8"))
	if send_data == 'bye':
		break
	print("".join(("接收内容：", str(sk.recv(1024),encoding="utf8"))))
sk.close()