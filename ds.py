class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]
 	 
     def show(self):
	     for x in reversed(self.items):
		      print x

     def size(self):
         return len(self.items)

class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def add(self, item):
		self.items.append(item)

	def remove(self):
		return self.items.remove(self.items[0])

	def show(self):
		for x in self.items:
			print(x)

	def size(self):
		return len(self.items)


