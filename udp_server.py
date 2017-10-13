import socket
import my_settings
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.bind((my_settings.UDP_IP, my_settings.UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    log_file = open(os.path.join(BASE_DIR, "log.txt"), 'a')
    log_file.write(str(addr[0])+"|"+str(addr[1])+"|"+data.decode())
    log_file.write("\n")
    log_file.flush()
    log_file.close()
    print("received message:", data.decode())
    print("address:", addr[0])
    print("port:", addr[1])
