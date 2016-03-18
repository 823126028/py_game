#expression = term {(&&)||(||)term};
#term = condtion || (extpretion);
#     a||b||c && e || f 
import lex.lex_getter;
import lex.token_manager;
import expr.condition_tree;
import expr.condition_leaf;
class task_parser:
	def __init__(self,token_manager):
		self.token_manager = token_manager;
		self.node_list = [];

	def expression(self):
		#print("in expression");
		condition_tree_1 = expr.condition_tree.condition_tree();
		condition_tree_1.add_child(self.term());

		while(self.token_manager.peak_token_n(1) and  (self.token_manager.peak_token_n(1).get_key() == "||" or self.token_manager.peak_token_n(1).get_key() == "&&")):
			if(condition_tree_1.compare_operand(self.token_manager.peak_token_n(1))):
				#print("in else one");
				self.token_manager.pop_token();
				condition_tree_1.add_child(self.term());
			else:
				#print("in else 2");
				condition_tree_2 = expr.condition_tree.condition_tree();
				condition_tree_2.add_child(condition_tree_1);
				condition_tree_2.set_operand(self.token_manager.pop_token());
				condition_tree_2.add_child(self.term());
				condition_tree_1 = condition_tree_2;
		return condition_tree_1;


	def term(self):
		#print("in term");
		token = self.token_manager.pop_token();
		if token.is_condtion_token():
			leaf = expr.condition_leaf.condition_leaf(token.get_key(),token.get_attribute_1());
			self.node_list.append(leaf);
			return leaf;
		elif token.is_token() and token.get_key() == "(":
			token_expression = self.expression();
			token_pop = self.token_manager.pop_token();
			if token_pop.is_token() and token_pop.get_key() == ")":
				return token_expression;
		return None;

	def parse(self):
		condition_tree_1 = self.expression();
		condition_tree_1.leaf_list = self.node_list;
		return condition_tree_1;

	def print_node_father(self):
		for node in self.node_list:
			father = node.get_root();
			print("father",father.operand.get_key());
	def test(self):
		for node in self.node_list:
			if node.left == "f":
					node.add_right_value(1);


if __name__ == '__main__':
	lex_getter_1 = lex.lex_getter.lex_getter();
	lex_getter_1.parse("[b>1]&&[d>2]&&[f:2]");
	#lex_getter_1.parse("[b:0]||[c>0]&&[e<6]");
	#lex_getter_1.print_token_list();
	token_manager_1 = lex.token_manager.token_manager(lex_getter_1.get_token_list());
	task_parser_1 = task_parser(token_manager_1)
	condition_1 = task_parser_1.parse();
	task_parser_1.print_node_father();
	print("total",condition_1.evalue());
	task_parser_1.test();
	print("total_2",condition_1.evalue());


			


