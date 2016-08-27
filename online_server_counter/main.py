import re;
import socket;
import struct;
import room_counter;
import chat_server_counter;
import threading;
import time;

def get_requet():
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(("127.0.0.1",9093));
    byte = "{\"pid\":1002}";
    pack = struct.pack('>i{0}s'.format(len(byte)),len(byte),byte.encode("utf-8"));
    sock.send(pack);
    data = b'';
    real_num,  = struct.unpack(">i",sock.recv(4));
    num = 0;
    while True:
        value=sock.recv(4096)     #把接收的数据定义为变量
        num = len(value) + num;
        if real_num <= num:
            data = data + value;
            break
        data = data + value;
    sock.close();
    return data.decode("utf-8");


def run_one_time():
    try:
       data = get_requet();
       rc = room_counter.RoomNumberCounter(data);
       cc = chat_server_counter.ChatServerCounter(data)
       rc.count_the_num();
       cc.count_all_num();
       rc.show();
       cc.show();
       a = time.localtime(time.time());
       x = time.strftime('%Y-%m-%d-%H-%M',a);
       print("已完成一次查询，请查看txt文件,当前时间" + x);
    except Exception as e:
        print(e);
    finally:
        pass;

def all_run():
    while True:
        run_one_time();
        time.sleep(1800)


if __name__ == "__main__":
    run_one_time();
    #all_run();


