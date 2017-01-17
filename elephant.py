from animal_class import Animal

class Elephant(Animal):

	def __init__(self, given_name, type, age, location, endangered):
		# We already know some qualities of an elephant
		self.given_name = given_name
		self.type = type
		self.age = age
		self.location = location
		self.endangered = endangered

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
		# Calling the parent constructor Animal to set the main attributes
		super().__init__("Elephant", "Mammal", 4, "herbivore", self.endangered)
		return("This %s is a %s.\nFeeding Habits: %s\nNo of Legs: %d\nEndangered: %s \
			\nGiven Name: %s\nType of Elephant: %s\nAge: %d\nLocation: %s"
			%(self.getName(), self.getAnimalClass(), self.getFeedingHabit(),
			 self.getNoOfLegs(), self.isEndangered(), self.given_name, self.type,
			 self.age, self.location))

	def showPolymorphism(self):
		print("\n ---- Testing Polymorphism... ----")
		return("This %s is a %s.\nFeeding Habits: %s\nNo of Legs: %d\nEndangered: %s \
			\nGiven Name: %s\nType of Elephant: %s\nAge: %d\nLocation: %s"
			%(self.getName(), self.getAnimalClass(), self.getFeedingHabit(),
			 self.getNoOfLegs(), self.isEndangered(), self.given_name, self.type,
			 self.age, self.location))

	def testEncapsulation(self):
		print("\n ---- Testing Encapsulation... ----")
		return("The name of this animal is: %s" % self.__name)



if __name__ == '__main__':
	try:
		elephant = Elephant("Tatu", "African", 50, "Maasai Mara", True)
		print(elephant.describeElephant())
	except Exception as e:
		print("Error: ", e)

	try:
		elephant = Elephant("Tatu", "African", 50, "Maasai Mara", True)
		print(elephant.showPolymorphism())
	except Exception as e:
		print("Error! Base Class Attributes overriden: ", e)

	try:
		print(elephant.testEncapsulation())
	except AttributeError as e:
		print("Encapsulation test: ", e)
