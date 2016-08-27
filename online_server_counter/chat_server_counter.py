import json;
import datetime
import time

class ChatServerCounter:
    def __init__(self,data):
        self.max_server = {};
        self.min_server = {};
        self.total_server = 0;
        self.total_num = 0;
        self.server_infos = {};
        self.data = data;

    def count_all_num(self):
        max_num = 0;
        min_num = 99999999;
        max_num_ip = "";
        min_num_ip = "";
        json_datas = json.loads(self.data);
        for json_data in json_datas["chatServerInfos"]:
            self.total_server += 1;
            num = int(json_data["userNumber"]);
            self.total_num += num;
            ip_port = json_data["ip"] + ":" + str(json_data["port"]);
            if num > max_num:
                max_num = num;
                max_num_ip = ip_port;
            if num <= min_num:
                min_num = num;
                min_num_ip = ip_port;
            self.server_infos[ip_port] = json_data;
        self.max_server[max_num_ip] = max_num;
        self.min_server[min_num_ip] = min_num;

    def show(self):
        x = time.localtime(time.time())
        s = time.strftime('%m-%d-%H-%M',x)
        fd = open("chat-server-info_" + s + ".txt","w");
        fd.write("最大的chat-msg:{0}".format(self.max_server) + "\n")
        fd.write("最小的chat-msg:{0}".format(self.min_server) + "\n")
        fd.write("chat-msg总人数:{0}".format(self.total_num) + "\n")
        fd.write("chat-msg总数目:{0}".format(self.total_server) + "\n");
        fd.write("所有server的数据\n");
        for key , server_info in self.server_infos.items():
            fd.write("ip:" + key + "  数据:{0}".format(server_info) + "\n");
        fd.flush();
        fd.close();
