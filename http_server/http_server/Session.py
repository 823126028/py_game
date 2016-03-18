import threading
import socket
import time
import struct;
import sys;
import Session;
import re;
buffSize = 1024;
pattern = re.compile(r"[a-zA-Z0-9]+#[a-zA-Z0-9]+");
class Session(threading.Thread):
	#address,session_id,write_buff,read_buff,is_auth
	def __init__(self,session_id,socket,address):#,session_manager):
		threading.Thread.__init__(self);
		self.session_id = session_id;
		self.address = address;
		self.write_buff = None;
		self.read_buff = None;
		self.is_auth = False;
		self.socket = socket;
		self.stop = False;
		#self.session_manager = session_manager;
		self.socket.setblocking(0);

	def write(self,obj):
		pass;

	#清除相关信息
	def do_close(self):
		#self.session_manager.remove(self.session_id);
		self.socket.close();
		self.stop = True;
		print("重置服务器线程=======");

	def run(self):
		while not self.stop:
			try:
				self.handle_read_object();
				self.handle_write_object();
			except Exception as e:
				print(e);
				print(type(e));
			time.sleep(1);

	def handle_read_object(self):
		data = None;
		try:
			data = self.socket.recv(buffSize);
			length = len(data);
			if length == 0:
				self.do_close();
			if self.read_buff:
				self.read_buff += data;
			else:
				self.read_buff = data;
		except BlockingIOError as e:
			print(e);
		except ConnectionAbortedError:
				#线程关闭了
				self.do_close();
		except ConnectionResetError as e:
				#对面关闭了socket
				self.do_close();
		try:
			value,tuple_value = self.protocl();
			if value:
				print("cmd:%s,data:%s"%((tuple_value[0].decode("UTF-8"),tuple_value[1].decode("UTF-8"))));
				self.handle_msg(tuple_value[0].decode("UTF-8"),tuple_value[1].decode("UTF-8"));
		except Exception as e:
			print(e);
			print("=====解析错误=====");
			self.do_close();

	def handle_msg(self,cmd,data):
		value = "I got it".encode("UTF-8");
		value2 = "I Have already got it".encode("UTF-8");
		key = pattern.match(cmd).group();
		if key == "cmd#hello":
			if self.write_buff:
				self.write_buff += struct.pack("%ds"%len(value),value);
			else:
				self.write_buff = struct.pack("%ds"%len(value),value);
		else:
			if self.write_buff:
				self.write_buff += struct.pack("%ds"%len(value2),value2);
			else:
				self.write_buff = struct.pack("%ds"%len(value2),value2);


	def handle_write_object(self):
		try:
			total_write_size = 0;
			if not self.write_buff:
				return;
			total_should_send_size = len(self.write_buff);
			while total_write_size < total_should_send_size:
				total_write_size += self.socket.send(self.write_buff);
			self.write_buff = None;
		except ConnectionResetError as e:
			#对面关闭了socket
			self.do_close();
		except BlockingIOError as e:
			print(e);
		except ConnectionAbortedError:
			#线程关闭了
			self.do_close();

	#4位总长度
	#32位key
	#data
	def protocl(self):
		if not self.read_buff:
			return False,None;
		if len(self.read_buff) <= 36:
			return False,None;
		size, = struct.unpack("i",self.read_buff[0:4]);
		if len(self.read_buff) < 36 + size:
			return False,None; 
		key, = struct.unpack("32s",self.read_buff[4:36]);
		data, = struct.unpack("%ds"%size,self.read_buff[36:36 + size]);
		self.read_buff = self.read_buff[36 + size:];
		return True,(key,data);
		


		

