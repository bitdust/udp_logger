from gevent import monkey
monkey.patch_all()
from bottle import route, run, response
import my_settings
import socket
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@route('/read_log')
def read_log():
    log_file = open(os.path.join(BASE_DIR, "log.txt"), 'r')
    log_str = log_file.read()
    log_file.close()
    response.content_type = "text/plain"
    return log_str


@route('/clear_log')
def clear_log():
    open(os.path.join(BASE_DIR, "log.txt"), 'w').close()
    response.content_type = "text/plain"
    return "done"


@route('/test_log')
def test_log():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    sock.sendto("test message".encode(), (my_settings.UDP_IP, my_settings.UDP_PORT))
    return "done"


@route('/readme')
def about():
    log_file = open(os.path.join(BASE_DIR, "readme.txt"), 'r')
    log_str = log_file.read()
    response.content_type = "text/plain"
    return log_str + "udp port=" + str(my_settings.UDP_PORT)

run(host=my_settings.WEB_IP, port=my_settings.WEB_PORT, server='gevent')
