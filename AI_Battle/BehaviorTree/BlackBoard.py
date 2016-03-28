class BlackBoard:
    def __init__(self):
        self.board_value = {};

    def put(self, key, value):
        self.board_value[key] = value;

    def get(self,key):
        return self.board_value.get(key);
