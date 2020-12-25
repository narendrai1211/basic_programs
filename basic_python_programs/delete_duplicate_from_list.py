string1 = 'hello'
list1 = []
list2 = []


def insert_record():
	list1.append(string1)
	list1.append(string1)
	print(list1)
	return list1


def duplicate_check(data):
	for i in d:
		if i not in list2:
			list2.append(i)
		else:
			pass
	print(list2)


data = insert_record()
duplicate_check(data)
