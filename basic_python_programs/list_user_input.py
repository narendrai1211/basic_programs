list_superheros = []


def user_input_superheros():
	while True:
		user_input = str(input("Enter name PRESS q to finish:"))
		if user_input == 'q' or user_input == 'Q':
			break
		else:
			list_superheros.append(user_input)
	return list_superheros


list_super = user_input_superheros()
print('The list is', list_super)
