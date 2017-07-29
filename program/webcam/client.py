import socket               # Import socket module
conn1 = socket.socket()
conn1.connect(('192.168.20.102', 1501))
while True:
    data = conn1.recv(10)
    print('%s' %data)
