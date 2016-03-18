import lex.normal_token;
class identify_token(lex.normal_token.normal_token):
	def __init__(self,key):
		lex.normal_token.normal_token.__init__(self,key);

	def is_condtion_token(self):
		return False;

	def is_token(self):
		return True;