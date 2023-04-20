import socket

ya_sock = socket.socket()
addr = ("77.88.55.242", 443)
ya_sock.connect(addr)
data_out = b"GET / HTTP/1.1\r\nHost:ya.ru\r\n\r\n"