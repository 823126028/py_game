游戏中的任务解析模块，根据任务条件和与或关系建语法树。


1.词法分析 
lex.lex_getter.py : 解析字符串中的单词 
identify_token.py : && || 这样的操作符
normal_token.py : 条件单词

2.语法分析:
task_parser.py

3.语法树
condition_tree.py   通过evalue 遍历来判断任务是否完成
condition_leaf.py 语法节点
