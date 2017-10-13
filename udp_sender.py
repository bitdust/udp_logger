import socket
import my_settings
MESSAGE = "hello222232".encode()

sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM) # UDP
sock.bind(('127.0.0.1',4221))
sock.sendto(MESSAGE, (my_settings.UDP_IP, my_settings.UDP_PORT))