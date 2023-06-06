class Animal:
	def makeNoise(self):
		raise 
class Cat(Animal):
	def makeNoise(self):
		print("MIAUUUU")

class Dog(Animal):
	def makeNoise(self):
		print("GUAUUU")

a = Cat();
a.makeNoise() 

a = Dog();
a.makeNoise() 