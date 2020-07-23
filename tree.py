class tree:
	def __init__(self, key, parent):
		self.parent = parent
		self.key = [key, []]

	def add_child(self, child):
		self.index = len(self.key[1])
		self.child = tree(child, self)
		self.key[1].append(self.child)
		return self.index
