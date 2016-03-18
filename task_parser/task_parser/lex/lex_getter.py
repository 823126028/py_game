from lex.condition_token import condition_token;
from lex.identify_token import identify_token;
import re;
class lex_getter:
	MAX_LENGTH = 32767;
	def __init__(self):
		self.token_list = [];
		# condition [kill:99] [kill > 99]
		self.pattern_condition = re.compile(r"(\[\s*(\w+)\s*([=:<>])\s*([0-9]+)\])");
		# 操作符 (   )  ||  &&
		self.pattern_token = re.compile("(\()|(\))|(\|\|)|(\&\&)");

	def parse(self,string_line):
		flag = True;
		while flag:
			if len(string_line) <= 0:
				break;
			# 两个condition和操作符不会相邻所以可以一次循环中 必然出现一次conditon 一次操作符
			#查询是否还有condition
			be_made_condition,a_condition_token,endpos_1 = self.make_condition_token(string_line);
			#查询是否还有操作符
			be_made_pattern,a_identify_token,endpos_2 = self.make_pattern_token(string_line);
			if not (be_made_condition or be_made_pattern):
				break;
			else:
				endpos = MAX_LENGTH;
				token_where = 0;
				if be_made_condition and endpos_1 < endpos:
						endpos = endpos_1;
						token_where = 1;
				if be_made_pattern and endpos_2 < endpos:
						endpos = endpos_2;
						token_where = 2;

				string_line = string_line[endpos:];
				if  token_where == 1:
					self.token_list.append(a_condition_token);
				else:
					self.token_list.append(a_identify_token);




	def print_token_list(self):
		for obj in self.token_list:
			print(obj.get_key());

	def get_token_list(self):
		return self.token_list;
			
					

	def make_condition_token(self,string_line):
		obj = self.pattern_condition.search(string_line);
		if obj:
			a_condition_token = condition_token(obj.group(0),obj.group(2),obj.group(3),obj.group(4));
			return True,a_condition_token,obj.end();
		else:
			return False,None,None;

	def make_pattern_token(self,string_line):
		obj = self.pattern_token.search(string_line);
		if obj:
			a_identify_token = identify_token(obj.group(0));
			return True,a_identify_token,obj.end();
		else:
			return False,None,None;


	


		
