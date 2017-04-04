import time
import matplotlib.pyplot as plt
import math

counter = {}
times = {}
lables = {}
stored_series = {}
stored_times = {}
stored_labels = {}
def method_decorator(method):
	'''
	Decorator to getter method invocations and execution times.
	'''

	def wrapper(*args, **kwargs):

		key = method
		if counter.__contains__(key) is False:
			counter[key] = 0
			times[key] = 0
			lables[key] = args[0].__module__
		init_time = time.time()
		response = method(*args, **kwargs)
		total_time = time.time() - init_time
		counter[key] += 1
		times[key] += total_time
		return response
	return wrapper

def reset_iteration_counters():
	'''
	Resets the iteration counters.
	'''
	counter.clear()
	times.clear()
	lables.clear()

def reset_counters():
	'''
	Resets all counters.
	'''
	counter.clear()
	times.clear()
	lables.clear()
	stored_series.clear()
	stored_times.clear()
	stored_labels.clear()

def store_iteration():
	'''
	Stores the iteration. Appends the iteration counter into store counters and reset the interation counters.
	'''
	for key, value in counter.iteritems(): 
		if stored_series.__contains__(key) is False:
			stored_series[key] = []
			stored_times[key] = []
			stored_labels[key] = lables[key]
		stored_series[key].append(value)
		stored_times[key].append(times[key])
	reset_iteration_counters()

def generate_report(filename="nroInteration.png"):
	'''
	Generates a report with stored invocation counters.
	'''
	plt.figure()
	x_series = range(2, stored_series.items()[0][1].__len__() + 2)
	for key, series in stored_series.iteritems():
		plt.plot(x_series, series, label=stored_labels[key])
	plt.legend(loc="upper left")
	plt.grid(True)
	plt.savefig(filename)