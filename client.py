import socket
import time
import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.153'
port = 8007
server = (host, port)
s.connect((host, port))

while 1:
    string = str(datetime.datetime.now())
    s.sendto(string.encode(), server)
    print('Message sent:', string)

    data = s.recv(1024)
    print('Answer: ', data.decode(), '\n')

    time.sleep(1)

s.close()
