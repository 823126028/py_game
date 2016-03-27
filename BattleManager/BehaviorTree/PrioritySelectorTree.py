from BehaviorTree.BTNode import BTNode;


class PrioritySelectorTree(BTNode):

    def __init__(self, name, precondition, cool_down, black_board):
        BTNode.__init__(self, name, precondition, cool_down, black_board);
        self.__active_node = None;

    def tick(self):
        BTNode.tick(self);
        done = self.__active_node.tick();
        if done:
            self.clear_expired_node();
            self.__active_node = None;
            return True;
        return False;

    def clear(self):
        self.__active_node = None;
        for child in self.children:
            child.clear();

    def clear_expired_node(self):
         if self.__active_node:
            self.__active_node.clear();
            self.__active_node = None;


    def do_evalue(self):
        for item in self.children.items():
            if item[1].meet_condition():
                if item[1] != self.__active_node:
                    self.clear_expired_node();
                self.__active_node = item[1];
                return True;
        return False;
