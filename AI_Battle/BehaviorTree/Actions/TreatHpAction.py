from BehaviorTree.Action import Action;
from event.TreatHpEvent import TreatHpEvent;


class TreatHpAction(Action):
    def __init__(self, name, precondition, cool_down, black_board):
        Action.__init__(self, name, precondition, cool_down, black_board);
        self.black_board = black_board;

    def choose_target(self):
        return self.black_board.get("self");

    def execute(self):
        battle = self.black_board.get("battle");
        target = self.choose_target();
        battle.add_event(TreatHpEvent(self.black_board.get("self"), target, battle));
