import time

counter = {}
times = {}
lables = {}
def method_decorator(method):

	def wrapper(*args, **kwargs):

		#key = method.__name__
		key = method
		#key = args[0]
		if counter.__contains__(key) is False:
			#print 'could not find method on counter:', counter
			counter[key] = 0
			times[key] = 0
			lables[key] = args[0].__module__
			# print 'entered decorator with method', method
			# print 'entered decorator with method.__name__', method.__name__
			#print 'entered decorator with method.im_class', method.im_class
			# print 'entered decorator with method.__class__', method.__class__
			# print 'entered decorator with args', args
			# print 'entered decorator with dir', dir(args[0])
			# print 'entered decorator with dir', args[0].__module__
			# print 'entered decorator with dir', dir(args[0].__module__)
			# print 'entered decorator with kwargs', kwargs
		init_time = time.time()
		response = method(*args, **kwargs)
		total_time = time.time() - init_time
		counter[key] += 1
		times[key] += total_time
		#print 'current count', counter[method]
		return response
	return wrapper

def reset_counters():
	#counter = {}
	#times = {}
	counter.clear()
	times.clear()
	lables.clear()

def generate_report():
	#TODO: implement ploting for methods
	pass