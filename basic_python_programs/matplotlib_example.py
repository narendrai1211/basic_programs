from matplotlib import pyplot as plt
import numpy


def plot_it(days_x, step_data_y):
	plt.plot(days_x, step_data_y, color='chocolate')
	plt.title('STEPS EACH DAY')
	plt.ylabel('Steps')
	plt.xlabel('Day')
	plt.show()


def calculate_things():
	str_y = '4284+14657+5473+3898+8151+9639+10571+4814+8644+11216+10647+9113+9327+15338'  # stored as string so that I can
	# also show u (list of str) to (list of int) conversion below
	days_x = [i for i in range(1, 15)]  # getting range between 1 to 14 inside a list
	split_char = '+'
	step_data_y = str_y.split(split_char)  # using split to covert string to python list, split character is '+'
	print(step_data_y)
	step_data_y = [int(i) for i in step_data_y]  # convert list of str to -> list of int
	print(days_x)
	numpy_mean = numpy.mean(step_data_y)
	print('Steps data mean', numpy_mean)
	plot_it(days_x, step_data_y)


calculate_things()
