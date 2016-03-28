import BehaviorTree.Precondition


class HpLessPercent(BehaviorTree.Precondition.Precondition):

    def __init__(self, percent, black_board):
        BehaviorTree.Precondition.Precondition.__init__(self, black_board)
        self.percent = percent;

    def check(self):
        if self.black_board.get("self").hp < self.black_board.get("self").max_hp * self.percent / 100:
            return True;
