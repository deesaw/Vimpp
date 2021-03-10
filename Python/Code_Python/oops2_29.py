class Dog:
	def speak(self):
		print("bhou..bhou")
	def guard(self):
		print("I am guarding")

tommy = Dog()
jimmy = Dog()

print(type(tommy))
print(isinstance(tommy,Dog))
tommy.speak()
jimmy.guard()