from EventManager import EventManager;
from event.HpReduceEvent import HpReduceEvent;


class FilterHpReduceEvent:

    def __init__(self, heater, target, battle,value):
        self.heater = heater;
        self.target = target;
        self.battle = battle;
        self.value = value;
        self.event_type = EventManager.FILTER_EFFECT_EVENT_KEY;

    def handle(self):
        delta_hp = max(1, self.value);

        # DO SOME THING ABOUT delta_hp

        self.battle.add_event(HpReduceEvent(self.heater, self.target, self.battle, delta_hp));