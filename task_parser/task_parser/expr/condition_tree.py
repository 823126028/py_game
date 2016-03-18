class condition_tree:
	def __init__(self):
		self.children_list = [];
		self.operand = None;
		self.father = None;
		self.leaf_list = [];
		self.last_value = False;

	def add_child(self,child):
		self.children_list.append(child);
		child.father = self;

	def set_operand(self,operand):
		self.operand = operand;

	def compare_operand(self,operand):
		if self.operand:
			return self.operand.get_key() == operand.get_key();
		else:
			self.operand = operand;
			return True;

	def evalue(self):
		if self.last_value:
			print(self.operand.get_key(),"use_last_key");
			return self.last_value;
		length_of_tree = len(self.children_list);
		if length_of_tree <= 0:
			return False;
		if length_of_tree == 1:
			self.last_value = self.children_list[0].evalue();
			return self.last_value;
		else:
			value = True;
			if self.operand.get_key() == "&&":
				for child in self.children_list:
					value = value and child.evalue();
					if not value:
						break;
				self.last_value = value;
				return value;
			else:
				value = False;
				for child in self.children_list:
					value = value or child.evalue();
				self.last_value = value;
				return value;


