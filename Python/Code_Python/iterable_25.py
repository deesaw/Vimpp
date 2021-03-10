class Car:
	def __init__(self,*passengers):
		self.seats=[]
		self.seats.extend(passengers)
	def __iter__(self):
		self.count = 0
		return self
	def __next__(self):
		if self.count < len(self.seats):
			output = self.seats[self.count]
			self.count+=1
			return output
		else:
			raise StopIteration

polo = Car('ravi','manisha','vamsi','naren','shefali')

for friend in polo:
	print(friend)

print(list(map(len,polo)))
