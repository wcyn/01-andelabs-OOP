# Super class / base class
class Animal:
	def __init__(self, name, animal_class, no_of_legs, feeding_habit, endangered=False):
		self.__name = name
		self.__animal_class = animal_class
		self.no_of_legs = no_of_legs
		self.feeding_habit = feeding_habit
		self.endangered = endangered

	def setEndangered(self,state):
		self.endangered = state

	def isEndangered(self):
		return self.endangered

	def setName(self, name):
		self.__name = name

	def getName(self):
		return self.__name

	def setAnimalClass(self, animal_class):
		self.__animal_class = animal_class

	def getAnimalClass(self):
		return self.__animal_class

	def setNoOfLegs(self, no_of_legs):
		self.no_of_legs = no_of_legs

	def getNoOfLegs(self):
		return self.no_of_legs

	def setFeedingHabit(self, feeding_habit):
		self.feeding_habit = feeding_habit

	def getFeedingHabit(self):
		return self.feeding_habit
