def divide(a,b):
	try:
		print(a/b)
	except Exception as err:
		print(type(err),err)
		print("Please check your denominator")


divide(5,2)
divide(5,0)