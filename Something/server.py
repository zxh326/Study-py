import socketserver
class myserver(socketserver.BaseRequestHandler):
	def handle(self):
		while True:
			conn = self.request
			addr = self.client_address
			while True:
				acc_data=str(conn.recv(1024),encoding="utf8")
				recv_data = str(addr[1])+ ':'+ acc_data
				conn.sendall(recv_data)
			conn.close()
if __name__ == '__main__':
	sever = socketserver.ThreadingTCPServer(("127.0.0.1", 8888),myserver)
	sever.serve_forever()