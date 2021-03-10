age = 16 # global

def grow():
	global age
	print(age)
	age = age + 1
	print(age)

print(age)
grow()