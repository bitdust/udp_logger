from bottle import route, run, response
import my_settings
import socket


@route('/read_log')
def read_log():
    log_file = open("log.txt", 'r')
    log_str = log_file.read()
    log_file.close()
    response.content_type = "text/plain"
    return log_str


@route('/clear_log')
def clear_log():
    open("log.txt", 'w').close()
    response.content_type = "text/plain"
    return "done"


@route('/test_log')
def test_log():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    sock.sendto("test message".encode(), (my_settings.UDP_IP, my_settings.UDP_PORT))
    return "done"


@route('/readme')
def about():
    log_file = open("readme.txt", 'r')
    log_str = log_file.read()
    response.content_type = "text/plain"
    return log_str + "udp port=" + str(my_settings.UDP_PORT)

run(host=my_settings.WEB_IP, port=my_settings.WEB_PORT)
