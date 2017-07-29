import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.20.10', 1500))
print 'Robot is connected'

while True:
    data = client.recv(10)
    print ('%s' %data)
    #if data[2]=='K':
    #    print
