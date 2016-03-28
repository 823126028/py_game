from BehaviorTree.Action import Action;
from event.NormalAttackEvent import NormalAttackEvent
import random;


class NormalAttackAction(Action):
    def __init__(self, name, precondition, cool_down, black_board):
        Action.__init__(self, name, precondition, cool_down, black_board);
        self.black_board = black_board;

    @staticmethod
    def choose_target(be_attacked_list):
        random_value = random.random();
        if random_value <= 0.3:
            return NormalAttackAction.strategy_weak(be_attacked_list);
        else:
            return NormalAttackAction.strategy_random(be_attacked_list);

    @staticmethod
    def strategy_weak(be_chosen_list):
        score = NormalAttackAction.get_target_score(be_chosen_list[0]);
        min_score_id = 0;
        for i in range(1, len(be_chosen_list)):
            if score >= NormalAttackAction.get_target_score(be_chosen_list[i]):
                min_score_id = i;
                score = NormalAttackAction.get_target_score(be_chosen_list[i]);
        return be_chosen_list[min_score_id];

    @staticmethod
    def strategy_random(be_chosen_list):
        return be_chosen_list[random.randint(0,len(be_chosen_list) - 1)];

    @staticmethod
    def get_target_score(be_attacked):
        return be_attacked.hp * 0.5 + be_attacked.attack * 1 - be_attacked.defend * 1.2;

    def execute(self):
        from battle import Battle;
        battle = self.black_board.get("battle");
        is_attack = self.black_board.get("side");
        target_list = [];
        if is_attack:
            target_list = list(Battle.get_all_alive(battle.defenders_list));
        else:
            target_list = list(Battle.get_all_alive(battle.attackers_list));

        target = self.choose_target(target_list);
        battle.add_event(NormalAttackEvent(self.black_board.get("self"), target, battle));
