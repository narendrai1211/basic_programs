str1 = 'Hello world f '
list1 = ['1', '2', '3', '4', '5', '6', '7']


def string_fx():
	print(str1.title())
	print(str1.split())
	print(str1.index('ll'))
	print(str1.join(list1))
	print(str1.strip())
	print(str1.replace('l', 'f'))
	print(str1.find('H'))
	print(str1.capitalize())
	print(str1.casefold())  # All capital to All small
	print(str1.center(0))
	print(str1.format(','))
	print(str1.isalnum())
	print(str1.partition('l'))
	print(str1.count('l'))
	print(str1.endswith('world f '))
	print(str1.encode())
	print(str1.isalpha())
	print(str1.isspace())
	print(str1.translate('H'))


string_fx()
