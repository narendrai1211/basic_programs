# Create Json file with python 
import json
list1 = []


def dictionary_append(): 
	ids = 1
	name = 'john doe'
	email = 'john.doe@example.com'
	temp_dict = {
		'id': ids, 
		'name': name,
		'email': email
	}
	list1.append(temp_dict)
	print(list1)
	return list1


def write_to_file():
	data = dictionary_append()
	dumped = json.dumps(data, indent=4, default=str)
	f = open('sample_data.json', 'w')
	f.write(dumped)
	f.close()


write_to_file()
