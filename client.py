#Chapter 1 Basics
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tar_ip = '127.0.0.1'
tar_port = 2222
sock.connect((tar_ip, tar_port))
sock.recv(1024).decode()
reply = 'Hey there!'.encode()
sock.send(reply)
sock.close()
sock.send(reply)
print(sock)