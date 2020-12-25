import random
list1 = []
list_num = []


def append_sachin():
	for i in range(1, 2 + 1):
		list1.append('sachin')


def append_nums():
	for i in range(1, 10 + 1):
		x = random.randint(1, 100)
		list_num.append(x)
	return list_num


def sort_tutorial():
	numbers = append_nums()
	print('original list ', numbers)
	numbers.sort()  # sorts the numbers and store it in same list
	print('everything is sorted\n', numbers)  # print the sorted list


def string_list_tutorial():
	append_sachin()
	print(list1)  # prints all elements of a list
	print(list1.count('sachin'))  # returns the count of a particular string
	print(list1.index('sachin'))  # returns the first occurrence of an element
	print(list1.clear())  # clears the list elements permanently
	print(list1)
	append_sachin()
	d = list1.remove('sachin')
	print(d)
	data = list1.copy()  # copies the list to another variable
	print(data)
	list1.insert(1, 'rahul')   # position to INSERT data and actual data
	print(list1)
	list2 = ['gambhir', 'msd']
	print(list1.extend(list2))   # takes an iterable as input and extends the list
	print(list1)
	list1.pop(2)   # removes the element from a list at a particular index
	print(list1)


string_list_tutorial()
sort_tutorial()
