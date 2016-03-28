from BehaviorTree.BTNode import BTNode;


class ParallelTree(BTNode):

        def __init__(self, name, precondition, cool_down, black_board, type):
            BTNode.__init__(self, name, precondition, cool_down, black_board);
            #type 1 all finish,meet_condition
            #type 0 one finish,meet_condition
            self.type = type;
            self.result_list = [];

        def add_child(self,node):
            BTNode.add_child(node);
            self.result_list.append(False);

        def resert_results(self):
            for key, value in enumerate(self.result_list):
                self.result_list[key] = False;

        def clear(self):
            self.resert_results();
            for child in self.children:
                child.clear();

        def do_evalue(self):
            for child in self.children:
                if not child.meet_condition():
                    return False;
            return True;

        def tick(self):
            end_num = 0;
            if self.type == 1:
                for key, child in self.children:
                    if not self.result_list[key]:
                        self.result_list[key] == child.meet_condition();
                        if self.result_list[key]:
                            self.resert_results();
                            return True;
            else:
                for key, child in self.children:
                    if not self.result_list[key]:
                        self.result_list[key] == child.meet_condition();
                        if self.result_list[key]:
                            end_num += 1;
            if end_num == len(self.result_list):
                self.resert_results();
                return True;




