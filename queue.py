class queue:
	def __init__(self):
		self.arr = []

	def enqueue(self, number):
		self.arr.append(number)

	def dequeue(self):
		value = self.arr[0]
		self.arr = self.arr[1:]
		return value
