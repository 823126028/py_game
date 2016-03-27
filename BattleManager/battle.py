from Monster import Monster;
from EventManager import EventManager;
from MsgManager import MsgManager;
import time;


class Battle:

    def __init__(self):
        self.attackers_list = [];
        self.defenders_list = [];
        self.frame = 0;
        self.msg_manager = MsgManager();
        self.event_manager = EventManager();

    def add_msg(self,msg):
        self.msg_manager.add_msg(msg);

    """
        战斗中的存活对象执行自己的操作
    """
    def execute_actors(self):
        alive_attack_actors = list(Battle.get_all_alive(self.attackers_list));
        alive_defend_actors = list(Battle.get_all_alive(self.defenders_list));

        for attacker in alive_attack_actors:
            attacker.run();
        for defender in alive_defend_actors:
            defender.run();

    def add_event(self,event):
        self.event_manager.get_event_list_by_key(event.event_type).append(event);

        """
        让怪物进入战场
    """
    def enter_battle(self,monsters,is_attackers):
        if is_attackers:
            self.attackers_list.extend(monsters);
        else:
            self.defenders_list.extend(monsters);

    @staticmethod
    def is_one_side_all_dead(side_list):
        for one in side_list:
            if one.hp > 0:
                    return False;
        return True;

    """
        检查比赛是否真的结束了
    """
    def is_end(self):
        if Battle.is_one_side_all_dead(self.defenders_list):
            self.msg_manager.add_msg("defenders all dead");
            return True;
        if Battle.is_one_side_all_dead(self.attackers_list):
            self.msg_manager.add_msg("attackers all dead");
            return True;
        return False;


    @staticmethod
    def get_all_alive(monster_list):
        return filter(lambda  attack:attack.hp > 0, monster_list);

    def do_one_frame(self):
        self.msg_manager.clear_one_round_msg();
        # 处理帧开始的事件,例如时间注册函数(buff到期,dot的执行和到期)
        self.event_manager.handle_event_list(EventManager.FRAME_EVENT_KEY);

        if self.is_end():
            print(self.msg_manager.send_msg());
            self.msg_manager.send_msg();
            return False;

        #执行玩家操作
        self.execute_actors();

        if self.is_end():
            self.msg_manager.send_msg();
            self.msg_manager.send_msg();
            return False;

        # 处理玩家操作使得使用的技能的事件
        self.event_manager.handle_event_list(EventManager.ACTION_EVENT_KEY);

        # 处理技能释放出来未经过处理的伤害增益buff等
        self.event_manager.handle_event_list(EventManager.FILTER_EFFECT_EVENT_KEY);

        # 处理实际最后增减释放过的伤害buff等
        self.event_manager.handle_event_list(EventManager.REAL_EFFECT_EVENT_KEY);

        if self.is_end():
            self.msg_manager.send_msg();
            self.msg_manager.send_msg();
            return False;
        self.msg_manager.send_msg();
        print("frame" + str(self.frame) + ":===================")
        time.sleep(2);
        return True;

    def all_run(self):
        while self.do_one_frame():
            self.frame += 1;


if __name__ == "__main__":
    battle = Battle();
    m_1 = Monster("attacker_1", 1, 30, 30, 40, 10);
    m_3 = Monster("attacker_2", 3, 30, 30, 40, 10);

    m_1.black_board.put("battle", battle);
    m_1.black_board.put("side", True);
    m_3.black_board.put("battle", battle);
    m_3.black_board.put("side", True);

    m_2 = Monster("defender_1", 2, 100, 100, 20, 20);
    m_4 = Monster("defender_2", 3 ,45, 45, 20, 20);

    m_2.black_board.put("battle", battle);
    m_2.black_board.put("side", False);
    m_4.black_board.put("battle", battle);
    m_4.black_board.put("side", False);

    attackers_list = [m_1, m_3];
    defenders_list = [m_2, m_4];
    battle.enter_battle(attackers_list, True);
    battle.enter_battle(defenders_list, False);
    battle.all_run();
