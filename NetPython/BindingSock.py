import socket
import sys

host = 'localhost'
port = 3306
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(5)

conn, add = s.accept()
print('connected to: ' + add[0] + ':' + str(add[1]))