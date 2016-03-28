from event.NormalAttackEvent import NormalAttackEvent
from TreeBuilder import TreeBuilder;
from BehaviorTree.BlackBoard import BlackBoard;
import random;


class Monster:

    def __init__(self, name, monster_id, hp, max_hp, attack, defend):
        self.name = name;
        self.monster_id = monster_id;
        self.hp = hp;
        self.max_hp = max_hp;
        self.attack = attack;
        self.defend = defend;
        self.black_board = BlackBoard();
        self.black_board.put("self",self);
        self.btNode = TreeBuilder.build_normal_ai(self.black_board);

    def run(self):
        self.btNode.run();




