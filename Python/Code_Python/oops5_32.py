from oops3 import Dog
class GuardDog(Dog):
	scientific_name = "Cannis Familiaris"
	_password = "ksfhoggosik"
	def __init__(self,color,breed,weight):
		super().__init__(color,breed)
		self.weight=weight
	def speak(self):
		print("grrr.grrr")
	def pspeak(self):
		super().speak()

tiger = GuardDog("Brown","Doberman",35)
tiger.speak()
tiger.guard()
tiger.pspeak()
print(tiger.weight)
print(tiger.scientific_name)
print(GuardDog.scientific_name)
#print(tiger._password)