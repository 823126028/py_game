from BehaviorTree.PrioritySelectorTree import PrioritySelectorTree;
from BehaviorTree.Actions.NormalAttackAction import NormalAttackAction;
from BehaviorTree.Actions.TreatHpAction import TreatHpAction;
from BehaviorTree.BlackBoard import BlackBoard;
from BehaviorTree.Preconditions.HpLessPercent import HpLessPercent;


class TreeBuilder:

    def __init__(self):
        pass;

    @staticmethod
    def build_normal_ai(black_board):
        root = PrioritySelectorTree("root", None, 1, black_board);
        root.add_child(TreatHpAction("treat_hp", HpLessPercent(70,black_board), 6, black_board));
        root.add_child(NormalAttackAction("normal_attack", None, 1, black_board));
        return root;

