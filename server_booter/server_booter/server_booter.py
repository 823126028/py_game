import threading;
import socket
import time;
import struct;
import sys;
import Session;


if __name__ == '__main__':
	s = socket.socket();
	s.bind(("127.0.0.1",8080));
	s.listen(1);
	s.listen(1);
	while True:
		socket,address = s.accept();
		session = Session.Session(socket,address);
		session.start();
		time.sleep(1);
