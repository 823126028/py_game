from EventManager import EventManager;
from event.FilterHpAddEvent import FilterHpAddEvent;


class TreatHpEvent:
    def __init__(self, heater, target, battle):
        self.heater = heater;
        self.target = target;
        self.battle = battle;
        self.event_type = EventManager.ACTION_EVENT_KEY;

    def handle(self):
        delta_hp = 15;
        self.battle.add_event(FilterHpAddEvent(self.heater, self.target, self.battle, delta_hp));