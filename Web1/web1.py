import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# the socket.socket() returns an object of the socket class

mysock.connect(('data.pr4e.org', 80))
# connect(('host', port))

