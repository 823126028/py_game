class MsgManager:

    def __init__(self):
        self.msg_list = [];

    def clear_one_round_msg(self):
        self.msg_list = [];

    def add_msg(self, msg):
        self.msg_list.append(msg);

    def send_msg(self):
        print(self.msg_list);