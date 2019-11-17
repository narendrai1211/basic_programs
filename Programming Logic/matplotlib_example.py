from matplotlib import pyplot as plt

str_y = '4284+14657+5473+3898+8151+9639+10571+4814+8644+11216+10647+9113+9327+15338'  # stored as string so that I can
# also show u list of str to list of int conversion below 
days_x = [i for i in range(1, 15)] #  getting range between 1 to 14 inside a list
step_data_y = str_y.split('+')  # using split to covert string to python list
print(step_data_y)
step_data_y = [int(i) for i in step_data_y]  # convert list of str to -> list of int
print(days_x)


def plot_it(): 
	plt.plot(days_x, step_data_y)
	plt.show()


plot_it()
