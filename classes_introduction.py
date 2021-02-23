#Everything in python is commonly referred as objects

class Person:
	pass

obj = Person()
a = Person()
# print(obj.)



l = ['a', 'b', 'c']
class Students():
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def student_name(self):
		print("Name is {}".format(self.name))

	def student_age(self):
		print("Age is {}".format(self.age))

s = Students("Shiva", 24)
# print(s.age)
# print(s.name)

# s.student_name()
# s.student_age()

# runtime modification
# s.age = 25
# print(s.age)