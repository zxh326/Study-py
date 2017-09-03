import socket
sk = socket.socket()
sk.bind(("127.0.0.1",8888))
sk.listen(5)
#rec
while True:	
	conn,addr = sk.accept()
	while True:
		accept_data = str(conn.recv(1024),encoding="utf8")
		print("".join(["接收内容：", accept_data,]))
		if accept_data=='bye':
			break
		#send
		send_data = input()
		conn.sendall(bytes(send_data,encoding="utf8"))
	conn.close()