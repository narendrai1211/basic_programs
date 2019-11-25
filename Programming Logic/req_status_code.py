import requests


def req_status_code():
	d = requests.get('https://www.google.co.in/')
	res_code = d.status_code
	success_status_code = 200
	if res_code is success_status_code:
		return res_code
	else:
		print('something is wrong')
		return 0


data = req_status_code()
print(data)
