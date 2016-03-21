import socket;
import threading;
import time;
import struct;
import sys;
log = open("client.txt","w+");
class ReadWriteThread(threading.Thread):
	def __init__(self,socket):
		super(ReadWriteThread,self).__init__();
		self.socket = socket;
		self.socket.setblocking(0);
	def run(self):
		strToSend = "200 Ok";
		byteToSend = struct.pack('32s',strToSend.encode('utf-8'));
		self.socket.send(byteToSend);
		while True:
			try:
				data = self.socket.recv(1024);
				str_data, = struct.unpack("32s",data);
				print(str_data.decode("utf-8"));
			except ConnectionResetError as e:
				self.socket.close();
				print("重置服务器线程=======");
				break;
			except BlockingIOError:
				pass;
			except ConnectionAbortedError:
				self.socket.close();
				print("重置服务器线程=======");
				break;
			except Exception as e:
				print(e);
			time.sleep(2);
if __name__ == '__main__':
	socket = socket.socket();
	socket.connect(("127.0.0.1",8080));
	readWriteThread = ReadWriteThread(socket);
	readWriteThread.start();
	time.sleep(1);
