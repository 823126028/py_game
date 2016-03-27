class EventManager:
    FRAME_EVENT_KEY = "frame";
    ACTION_EVENT_KEY = "action";
    FILTER_EFFECT_EVENT_KEY = "filter";
    REAL_EFFECT_EVENT_KEY = "real";

    def __init__(self):
        # frame event 每一帧开始的时候执行的事情
        self.frame_event_list = [];
        # 处理对象自己发出的动作的操作,向下发出伤血
        self.action_event_list = [];
        # 未经过什么buff处理的伤血,和增益buff,减益buff
        self.filter_effect_event_list = [];
        # 实际造成的伤血效果,buff效果,战斗效果
        self.real_effect_event_list = [];

    """
        产生新的队列，是为了让让本次扫描扫产生的同类型的消息等到下次处理
    """
    def swap_new_event_by_key(self, key):
        if key == EventManager.FRAME_EVENT_KEY:
            self.frame_event_list = [];
        elif key == EventManager.ACTION_EVENT_KEY:
            self.action_event_list = [];
        elif key == EventManager.FILTER_EFFECT_EVENT_KEY:
            self.filter_effect_event_list = [];
        else:
            self.real_effect_event_list = [];

    """
        产生新的队列，是为了让让本次扫描扫产生的同类型的消息等到下次处理
    """
    def handle_event_list(self, key):
        event_list = self.get_event_list_by_key(key);
        self.swap_new_event_by_key(key);
        for event in event_list:
            event.handle();

    """
        通过key来获得各个层次的消息事件
    """
    def get_event_list_by_key(self,key):
        if key == EventManager.FRAME_EVENT_KEY:
            return self.frame_event_list;
        elif key == EventManager.ACTION_EVENT_KEY:
            return self.action_event_list;
        elif key == EventManager.FILTER_EFFECT_EVENT_KEY:
            return self.filter_effect_event_list;
        else:
            return self.real_effect_event_list;