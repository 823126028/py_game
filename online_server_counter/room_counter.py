import re;
import time;
import datetime;

class RoomNumberCounter:
    def __init__(self,data):
        self.max_room = {};
        self.min_room = {};
        self.total_room = 0;
        self.total_num = 0;
        self.room_num = {};
        self.data = data;

    def get_all_num_list(self):
        p = re.compile(r'{\"userNumber\":[0-9]+,\"roomId\":\"[0-9]+\"}');
        return p.findall(self.data);

    def count_the_num(self):
        element_list = self.get_all_num_list();
        max_room_num = 0;
        max_room_id = 0;
        min_room_num = 999999999;
        min_room_id = 0;
        for element in element_list:
            num_str, room_str = element.split(",");
            num = int(num_str.split(":")[1]);
            room_id = int(room_str.split(":")[1][1:-2]);
            self.total_num += num;
            self.total_room += 1;
            self.room_num[room_id] = num;
            if num > max_room_num:
                max_room_num = num;
                max_room_id = room_id;
            if num < min_room_num:
                min_room_num = num;
                min_room_id = room_id
        self.max_room[max_room_id] = max_room_num;
        self.min_room[min_room_id] = min_room_num;

    def show(self):
        x = time.localtime(time.time())
        s = time.strftime('%m-%d-%H-%M',x)
        fd = open("chat-room-info_" + s + ".txt" ,"w");
        fd.write("人数最大房间id:数量{0} ".format(self.max_room) + "\n");
        fd.write(("人数最少房间id:数量{0} ").format(self.min_room) + "\n");
        fd.write("总人数:{0} ".format(self.total_num) + "\n");
        fd.write("总房间数:{0} ".format(self.total_room) + "\n");
        fd.write("所有的房间数据\n");
        for key, num in self.room_num.items():
            fd.write("room_id :" + str(key) + ";num :" + str(num) + "\n");
        fd.flush();
        fd.close();