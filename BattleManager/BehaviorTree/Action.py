from BehaviorTree.BTNode import  BTNode


class Action(BTNode):

    def __init__(self, name, precondition, cool_down, black_board):
        BTNode.__init__(self, name, precondition, cool_down, black_board);
        self.black_board = black_board;

    def tick(self):
        BTNode.tick(self);
        return self.execute();

    def execute(self):
        pass;
