class condition_leaf:
	def __init__(self,condition_key,attribute_tuple):
		self.condition_key = condition_key;
		self.split_handle_condition(attribute_tuple);
		self.__init_value_for_test();
		self.last_value = False;
		
	#condition 的格式 kill < 9 之类的所以要解析condition
	def split_handle_condition(self,attribute_tuple):
		self.condition_name = attribute_tuple[0];
		self.condition_value = int(attribute_tuple[2]);
		self.op = attribute_tuple[1];
	
	#获得父亲节点数据	
	def get_root(self):
		father = self.father;
		while father.father:
			father = self.father;
		return father;
	
	#算出该节点是否满足条件,如果满足条件设置last_value为true。这样就避免了下次继续访问	
	def evalue(self):
		if self.last_value:
			print(self.condition_key,"use_last_value");
			return self.last_value;
		value = False;
		if self.op == ">":
			value = self.value_collection[self.condition_name] > self.condition_value;
		elif self.op == "<":
			value = self.value_collection[self.condition_name] > self.condition_value;
		elif self.op == ":":
			value = self.value_collection[self.condition_name] == self.condition_value;
		elif self.op == "==":
			value = self.value_collection[self.condition_name] == self.condition_value;
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
