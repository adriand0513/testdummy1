class BalancedStack:
	def __init__(self):
		self.stack = []
		
	def is_empty(self):
		return len(self.stack) == 0 
		
	def push(self, char):
		self.stack.append(char)
		
	def pop(self):
		if not self.is_empty():
			return self.stack.pop()
		else:
			raise IndexError("pop from an empty stack.")
	
	def is_balanced(self, expression):
		opening_brackets = "({[<"
		closing_brackets = ")}]>"
		
		for char in expression:
			if char in opening_brackets:
				self.push(char)
			elif char in closing_brackets:
				if self.is_empty() or closing_brackets.index(char) != opening_brackets.index(self.pop()):
					return False
		return self.is_empty()
		

my_stack = BalancedStack()
expression = "<{{{1234>"
result = my_stack.is_balanced(expression)
print(result)
