import time;


class BTNode:

    def __init__(self, name, precondition, cool_down, black_board):
        self.precondition = precondition;
        self.last_tick_time = 0;
        self.cool_down = cool_down;
        self.name = name;
        self.children = {};
        self.black_board = black_board;

    def add_child(self,node):
        self.children[node.name] = node;

    def remove_child(self,node):
        return self.children.pop(node.name);

    def is_cool_down(self):
        is_cool_down = self.last_tick_time + self.cool_down < time.time();
        return is_cool_down;

    def run(self):
        if self.meet_condition():
            self.tick();

    def meet_condition(self):
        return (not self.precondition or self.precondition.check())  and self.is_cool_down() and self.do_evalue();

    def do_evalue(self):
        return True;

    def tick(self):
        self.last_tick_time = time.time();
        return True;

    def clear(self):
        pass;