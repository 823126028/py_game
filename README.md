平时写的一些用py写过的一些游戏组件

task_parser:
    游戏中的任务解析模块，根据任务条件和与或关系建语法树。
    如 kill:99 && gold > 100 || wood = 1000
    1.词法分析 
    2.语法分析:
    3.语法树
    4.根据语法树求值

segment_tree: 用于游戏中海量数据排序的线段树算法

server_booter:用python 写的OIO网络端程序


AI_BATTLE :模拟一些即时类战略游戏的AI战斗的项目
1. 使用分层事件处理机制来处理AI和玩家的行为来降低耦合性,把玩家事件分为frame_effect(每一帧处理的时间), action_effect(玩家动作和技能), filter_effect(未经过滤伤害和技能), real_effect(实际的伤害和技能)。
2. 使用行为树作为AI_NODE,分为(结构型)PrioritySelector(选择执行树), SequenceSelector(顺序执行树), ParallelSelector(并行执行树).(Precondition) 条件型 和(Action) 实际动作型。通过行为树来代替状态机来操作AI
