from EventManager import EventManager;


class HpAddEvent:
    def __init__(self, heater, target, battle, value):
        self.heater = heater;
        self.target = target;
        self.battle = battle;
        self.value = value;
        self.event_type = EventManager.REAL_EFFECT_EVENT_KEY;

    def handle(self):
        self.target.hp += self.value;
        self.battle.add_msg(self.heater.name + " add hp to " + self.target.name  + " hpz: " +  str(self.value));
