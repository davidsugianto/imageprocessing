import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 1500))
while True:
        print'receiving data...'
        data = client.recv(1024)
        client.send('siap kapten')
        print('%s' %data)
        if not data:
            break


                       
 
