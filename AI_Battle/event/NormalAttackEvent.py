from EventManager import EventManager;
from event.FilterHpReduceEvent import FilterHpReduceEvent;


class NormalAttackEvent:

    def __init__(self, attacker, target, battle):
        self.attacker = attacker;
        self.target = target;
        self.battle = battle;
        self.event_type = EventManager.ACTION_EVENT_KEY;

    def handle(self):
        delta_hp = self.attacker.attack - self.target.defend;
        self.battle.add_event(FilterHpReduceEvent(self.attacker, self.target, self.battle, delta_hp));


