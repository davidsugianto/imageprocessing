import socket

robot = socket.socket()
robot.connect(('192.168.1.102', 28097))

while True:
	data = client.recv(1024)
	print('%s' %data)
	if not data:
		break
