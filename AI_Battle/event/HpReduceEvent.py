from EventManager import EventManager;


class HpReduceEvent:

    def __init__(self, attacker, target, battle, value):
        self.attacker = attacker;
        self.target = target;
        self.battle = battle;
        self.value = value;
        self.event_type = EventManager.REAL_EFFECT_EVENT_KEY;

    def handle(self):
        self.target.hp -= self.value;
        self.battle.add_msg(self.attacker.name + " attack " + self.target.name + " damage " + str(self.value));
