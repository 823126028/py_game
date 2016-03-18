class condition_leaf:
	def __init__(self,condition_key,attribute_tuple):
		self.condition_key = condition_key;
		self.split_handle_condition(attribute_tuple);
		self.__init_value_for_test();
		self.last_value = False;

	def split_handle_condition(self,attribute_tuple):
		self.left = attribute_tuple[0];
		self.right = int(attribute_tuple[2]);
		self.op = attribute_tuple[1];

	def add_right_value(self,num):
		self.right += num;

	def get_root(self):
		father = self.father;
		while father.father:
			father = self.father;
		return father;
			
	def evalue(self):
		if self.last_value:
			print(self.condition_key,"use_last_value");
			return self.last_value;
		value = False;
		if self.op == ">":
			value = self.value_collection[self.left] > self.right;
		elif self.op == "<":
			value = self.value_collection[self.left] > self.right;
		elif self.op == ":":
			value = self.value_collection[self.left] == self.right;
		elif self.op == "==":
			value = self.value_collection[self.left] == self.right;
		else:
			print("condition_key",self.condition_key);
			return False;
		self.last_value = value;
		print("key",self.condition_key,value);
		return value;

	def __init_value_for_test(self):
		self.value_collection = {};
		self.value_collection["a"] = 5;
		self.value_collection["b"] = 6;
		self.value_collection["c"] = 11;
		self.value_collection["d"] = 12;
		self.value_collection["f"] = 3;