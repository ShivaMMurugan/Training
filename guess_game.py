import random
user_input = int(input("Enter a number between 1 to 20: "))
choice = 1
while choice < 7:
	number = random.randrange(20)
	if user_input != number:
		choice += 1
		print("choice used, {}".format(choice))
		user_input = int(input("Enter a number between 1 to 20: "))
		if choice == 7:
			print("Sorry you have used all choices")
			break
	else:
		print("You have guessed the right answer", number)
		break