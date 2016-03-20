from segment import Segment
from node import Node

class SegmentTree:
	def __init__(self,min_value,max_value):
		self.root = Segment((min_value,max_value),None,None,None);
	
	"""
		线段树利用递归建树。
	"""
	def build_tree(self,father_segment):
		max_value = (int)(father_segment.ranges[1]);
		min_value = (int)(father_segment.ranges[0]);
		mid = (int)((max_value + min_value) / 2);
		if max_value <= min_value:
			return;
		father_segment.left = Segment((min_value,mid),father_segment,None,None);
		father_segment.right = Segment((mid + 1,max_value),father_segment,None,None);
		self.build_tree(father_segment.left);
		self.build_tree(father_segment.right);
	
	"""
		中续遍历二叉树
	"""
	def print_all_tree(self,father_segment):
		if not father_segment:
			return; 
		print("========")
		print("head---",father_segment.ranges);
		print("segment---",father_segment.num);
		head = father_segment.head;
		while head.next:
			print("node",head.next.pid);
			print("ranks",head.next.get_rankers());
			head = head.next;
		self.print_all_tree(father_segment.left);
		self.print_all_tree(father_segment.right);


	"""
		将node的玩家数据放入线段树的枝叶中
	"""
	def down_to_segment(self,segment,node):
		if not segment :
			return;
		if segment.left.in_range(node):
			if segment.left.is_leaf():
				node.add_to_new_segment(segment.left);
				return;
			else:
				self.down_to_segment(segment.left,node)
				return;

		if segment.right.in_range(node):
			if segment.right.is_leaf():
				node.add_to_new_segment(segment.right);
				return;
			else:
				self.down_to_segment(segment.right,node);
				return;
		print("down_to_segment.........out of range ");



if __name__ == '__main__':
	segmentTree = SegmentTree(1,10);
	segmentTree.build_tree(segmentTree.root);
	node = Node("gabriel");
	node.value = 6;
	node2 = Node("chen");
	node2.value = 3;
	segmentTree.down_to_segment(segmentTree.root,node);
	segmentTree.down_to_segment(segmentTree.root,node2)
	segmentTree.print_all_tree(segmentTree.root);


		
