class token_manager:
	def __init__(self,token_list):
		self.token_list = token_list;
		self.token_index = 0;

	def peak_token_n(self,n):
		if n < 1:
			n = 1; 
		index = self.token_index - 1 + n;
		if  index >= len(self.token_list):
			return None
		else:
			return self.token_list[index];

	def is_empty(self):
		if self.token_index  >=  len(self.token_list):
			return True;
		else:
			return False;

	def pop_token(self):
		obj = self.token_list[self.token_index];
		#print("pop_token",obj.get_key());
		self.token_index = self.token_index + 1;
		return obj;

