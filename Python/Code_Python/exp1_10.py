while True:
	try:
		amount = int(input("Enter the amount you wish to withdraw: "))
		print("Pl. collect your cash")
		break
	except ValueError:
		print("Please enter a valid amount")