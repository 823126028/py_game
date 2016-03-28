from BehaviorTree.BTNode import BTNode;


class SequenceTree(BTNode):

        def __init__(self, name, precondition, cool_down, black_board):
            BTNode.__init__(self, name, precondition, cool_down, black_board);
            self.__active_index = -1;

        def clear(self):
            self.__active_index = -1;
            for child in self.children:
                child.clear();

        def clear_expired_node(self):
             if self.__active_index >= 0:
                self.children[self.__active_index].clear();
                self.__active_index = -1;

        def do_evalue(self):
            if self.__active_index == -1:
                if self.children[0].meet_condition():
                    self.__active_index = 0;
                    return True;
            else:
                if self.children[self.__active_index].meet_condition():
                    return True;
                self.clear_expired_node();
            return False;

        def tick(self):
            super.tick();
            done = self.children[self.__active_index].tick();
            if done:
                self.__active_index += 1;
                if self.__active_index >= len(self.children):
                    self.clear_expired_node();
                done = False;
            return done;




