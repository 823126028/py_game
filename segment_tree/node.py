class Node:
	def __init__(self,pid):
		self.pid = pid;
		self.value = 0;
		self.next = None;
		self.prev = None;
		self.segment = None;

	def add_to_new_segment(self,segment):
		if self.segment:
			if self.segment == segment:
				return;
			else:
				print("#remove out")
				self.remove_node_out_segment();
		segment.add_to_segment_list(self);
		temp_segment =  segment;
		while temp_segment:
			temp_segment.num += 1;
			temp_segment = temp_segment.parent;
		self.segment = segment;


	#获得该玩家信息节点，在所有线段树中的排名
	def get_rankers(self):
		if self.segment:
			if self.segment.parent:
				if self.segment.parent.left == self.segment:
					return self.segment.parent.num + 1;
				else:
					return self.segment.parent.left.num + 1;

			else:
				return 1;


		else:
			return 0;

	#将节点从之前的线段树中移除
	def remove_node_out_segment(self):
		if not self.segment:
			return;
		if self.next:
			self.next.prev = self.prev;
		self.prev.next = self.next;
		self.next = None;
		self.prev = None;
		segment = self.segment;
		while segment:
			print("#remove segment",segment.ranges);
			segment.num -= 1;
			segment = segment.parent;
					
