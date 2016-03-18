class normal_token:
	def __init__(self,key):
		self.key = key;
	def is_condtion_token(self):
		return False;

	def is_token(self):
		return False;

	def get_key(self):
		return self.key;