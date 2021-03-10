#Advanced OOPS
# Understanding Duck typing
# Understanding str,len,bool methods
# Operator Emulation

class Car:
	def __init__(self,seats,regno=None):
		self.seats = seats
		self.regno = regno
	def __str__(self):
		return "I am a {} seater car".format(self.seats)
	def __len__(self):
		return self.seats
	def __bool__(self):
		if self.regno:
			return True
		else:
			return False
	def __add__(self,other):
		return self.seats + other.seats

polo   = Car(5)
innova = Car(7,'TS05 9834')

print(polo)
print(innova)

k = str(polo)
print(k)

print(len(polo))
print(len(innova))

print("polo",bool(polo))
print("innova",bool(innova))

print(polo + innova)
