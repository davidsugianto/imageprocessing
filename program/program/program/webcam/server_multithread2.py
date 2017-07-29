import socket
#from threading import Thread

#def clientHandler():
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 1500))
server.listen(5)
print 'Waiting for incoming connections...'
conn, addr = server.accept()
print (addr, 'is connected')

message = raw_input("->")
while message != 'q':
        conn.send(message)
        data = conn.recv(1024)
        message = raw_input('->')
        print 'Received data', repr(data)
        if not data:
            break

#message = raw_input('->')

#for i in range(5):
#    Thread(target=clientHandler).start()

