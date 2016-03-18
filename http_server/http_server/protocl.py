import struct;

def test():
	s = struct.pack("i",10);
	s1 = struct.pack("2s","dd".encode("utf-8"));
	s2 = s + s1;
	i, = struct.unpack("i",s2[0:4]);
	print(i);

if __name__ == '__main__':
	test();
