def divide(a,b):
	try:
		result = a/b
	except ZeroDivisionError:
		print("Please check your denominator")
	else:
		print(result)
	finally:
		print("this is the finally block")


divide(5,2)
divide(5,0)
divide("a","b")