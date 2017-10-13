log the simple udp message and the sender's IP & port.

=======how to use=======
/read_log
read all udp log

/clear_log
clear all log

/test_log
send a test message to local udp port

/readme
some help message

=======how to deploy=======
0.requires python3.6+ & python3-bottle
1.modify my_settings.py
2.run udp_server.py & web_server.py
3.test the service by access /test_log or send a simple string to the udp port

