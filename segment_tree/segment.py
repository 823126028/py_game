from node import Node
#线段树的枝叶
class Segment:
	def __init__(self,ranges,parent,left,right):
		self.left = left;
		self.right = right;
		self.ranges = ranges;
		self.parent = parent;
		self.ranges = ranges;
		#线段树枝叶中存放玩家信息的Node的头节点
		self.head = Node(0);
		#该线段树节点中的玩家信息数量
		self.num = 0;

	#判断该线段树是否是叶子
	def is_leaf(self):
		if self.left or self.right:
			return False;
		return True;

	#判断是否在该节点内
	def in_range(self,node):
		if node.value <= self.ranges[1] and node.value >= self.ranges[0]:
			return True;
		return False;

	#将节点用前插法插入
	def add_to_segment_list(self,node):
		if self.head.next:
			self.head.next.prev = node.next;
			node.next = self.head.next;
		node.prev = self.head;
		self.head.next = node;

		

		