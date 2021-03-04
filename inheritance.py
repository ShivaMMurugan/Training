class Employee():
	def __init__(self, first, last, email):
		self.first = first
		self.last = last
		self.email = email

	def first_name(self):
		return f'Firstname {self.first}'
	def last_name(self):
		return f'Lastname {self.last}'


# e1 = Employee("Siva", "Murugan", "Siva.Murugan@email.com")
# print(e1.first)

class Developer(Employee):
	def __init__(self, first, last, email, prog_lang):
		super().__init__(first, last, email)
		self.prog_lang = prog_lang

d1 = Developer("Siva", "Murugan", "Siva.Murugan@email.com", "Python")
print(d1.prog_lang)


