from animal_class import Animal

class Elephant(Animal):

	def __init__(self, given_name, type, age, location, endangered, has_tusks=True):
		# We already know some qualities of an elephant
		# Calling the parent constructor Animal to set the main attributes
		super().__init__("Elephant", "Mammal", 4, "herbivore", endangered)
		self.given_name = given_name
		self.type = type
		self.has_tusks = has_tusks
		self.age = age
		self.location = location

	def setGivenName(self, given_name):
		self.given_name = given_name

	def getGivenName(self):
		return self.given_name

	def setType(self, type):
		self.type = type

	def getType(self):
		return self.type

	def setAge(self, age):
		self.age = age

	def getAge(self):
		return self.age

	def setLocation(self, location):
		self.location = location

	def getLocation(self):
		return self.location

	def describeElephant(self):
		return("This %s is a %s.\nFeeding Habits: %s\nNo of Legs: %d\nEndangered: %s \
			\nGiven Name: %s\nType of Elephant: %s\nHas Tusks: %s\nAge: %d\nLocation: %s"
			%(self.getName(), self.getAnimalClass(), self.getFeedingHabit(),
			 self.getNoOfLegs(), self.isEndangered(), self.given_name, self.type, self.has_tusks,
			 self.age, self.location))



if __name__ == '__main__':
	elephant = Elephant("Tatu", "African", 50, "Maasai Mara", True)
	print(elephant.describeElephant())
