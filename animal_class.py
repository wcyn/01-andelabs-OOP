# Super class / base class
class Animal:
	def __init__(self, name, endangered=False, animal_class, no_of_legs, feeding_habit):
		self.name = name
		self.animal_class = animal_class
		self.no_of_legs = no_of_legs
		self.feeding_habit = feeding_habit
		self.endangered = endangered

	def setEndangered(self,state):
		self.endangered = state

	def getEndangered():
		return self.endangered

	def setName(name):
		self.name = name

	def getName():
		return self.name

	def setAnimalClass(animal_class):
		self.animal_class = animal_class

	def getAnimalClass(animal_class):
		return self.animal_class

	def setNoOfLegs(no_of_legs):
		self.no_of_legs = no_of_legs

	def getNoOfLegs(no_of_legs):
		return self.no_of_legs

	def setFeedingHabit(feeding_habit):
		self.feeding_habit = feeding_habit

	def getFeedingHabit(feeding_habit):
		return self.feeding_habit
