import threading
import socket
import time
import struct;
import sys;
log = open("log.txt","w+");
buffSize = 1024;
socket_num = 1; 
class ReadThread(threading.Thread):
	def __init__(self,socket):
		super(ReadThread, self).__init__();
		self.socket = socket;
		self.socket.setblocking(0);
	def run(self):
		while True:
			data = None;
			try:
				data = self.socket.recv(buffSize);
				length = len(data);
				if length == 0:
					self.socket.close();
					print("重置服务器线程=======");
					break;
				s, = struct.unpack("%ds"%(length),data);
				print(s.decode('utf-8'));
				str = """HTTP/1.1 200 OK
						Cache-Control: private, max-age=0
						Date: Fri, 02 Jan 2009 12:26:17 GMT
						Expires: -1
						Content-Type: text/html; charset=GB2312
						\r\n
						<html>
							<h5>html</h5>
						</html>
						""";
				ss = struct.pack("%ds"%len(str),str.encode("utf-8"));
				self.socket.send(ss);
			except ConnectionResetError as e:
				self.socket.close();
				print("重置服务器线程=======");
				break;
			except BlockingIOError as e:
				print(e);
			except ConnectionAbortedError:
				self.socket.close();
				print("重置服务器线程=======");
				break;
			except Exception as e:
				print(e);
				print(type(e));
			time.sleep(2);


if __name__ == '__main__':
	s = socket.socket();
	s.bind(("127.0.0.1",8080));
	s.listen(1);
	while True:
		conn,addr = s.accept();
		readThread = ReadThread(conn);
		readThread.start();
		time.sleep(1);
