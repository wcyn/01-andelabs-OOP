from animal_class import Animal

class Elephant(Animal):
	def __init__(self, given_name, type, has_tusks=True, age, location):
		self.given_name = given_name
		self.type = type
		self.has_tusks = has_tusks
		self.age = age
		self.location = location

	def setGivenName(given_name):
		self.given_name = given_name

	def getGivenName(given_name):
		return self.given_name

	def setType(type):
		self.type = type

	def getType(type):
		return self.type

	def setAge(age):
		self.age = age

	def getAge(age):
		return self.age

	def setLocation(location):
		self.location = location

	def getLocation(location):
		return self.location


