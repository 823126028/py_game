import lex.normal_token;
class condition_token(lex.normal_token.normal_token):
	def __init__(self,key,intrest,op,target):
		lex.normal_token.normal_token.__init__(self,key);
		self.intrest = intrest;
		self.op = op;
		self.target = target;

	def get_attribute_1(self):
		return (self.intrest,self.op,self.target);
		
	def is_condtion_token(self):
		return True;

	def is_token(self):
		return False;
