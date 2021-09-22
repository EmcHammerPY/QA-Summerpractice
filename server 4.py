import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostbyname(''))
port = 8007
s.bind((host, port))

print('- Server Start - ')
s.listen(1)
conn, addr = s.accept()
print('Client connected:', addr[0])

while 1:
    data = conn.recv(1024)
    print('Message from', addr[0], ':', data.decode())
    second = int(data.decode()[-9:-7])
    if second % 2 == 0:
        conn.send('Number is pair'.encode())
    else:
        conn.send('Number isn\'t pair'.encode())
conn.close()

