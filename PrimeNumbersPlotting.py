version = '0.1'
series0 = []
series1 = []
series2 = []
series3 = []
series4 = []
series5 = []
series = [series0, series1, series2, series3, series4, series5]

executions = {}

import math
def generate_primes3(limit):
	primes = []
	iterations = 0
	for i in range(2, limit + 1):
		count = 0
		for j in range(1,int(math.sqrt(i) + 1)):
			iterations = iterations + 1
			if i % j == 0:
				count = count + 1
		if count == 1:
			primes.append(i)
			if count > 1:
					break
	series3.append(iterations)
	executions[generate_primes3] = (series3, primes)

def generate_primes2(limit):
	primes = []
	iterations = 0
	for i in range(2, limit + 1):
		count = 0
		for j in range(1,(i/2) + 1):
			iterations = iterations + 1
			if i % j == 0:
				count = count + 1
				if count > 1:
					break
		if count <= 1:
			primes.append(i)
	series2.append(iterations)
	executions[generate_primes2] = (series2, primes)

def generate_primes1(limit):
	primes = []
	iterations = 0
	for i in range(2, limit + 1):
		count = 0
		for j in range(1,i):
			iterations = iterations + 1
			if i % j == 0:
				count = count + 1
				if count > 1:
					break
		if count <= 1:
			primes.append(i)
	series1.append(iterations)
	executions[generate_primes1] = (series1, primes)

def generate_primes0(limit):
	primes = []
	iterations = 0
	for i in range(2, limit + 1):
		count = 0
		for j in range(1,i):
			iterations = iterations + 1
			if i % j == 0:
				count = count + 1
		if count <= 1:
			primes.append(i)
	series0.append(iterations)
	executions[generate_primes0] = (series0, primes)

def generate_primes4(limit):
	primes = []
	iterations = 0
	for i in range(2, limit + 1):
		for j in primes:
			iterations = iterations + 1
			if i % j == 0:
				break
		else:
			primes.append(i)
	series4.append(iterations)
	executions[generate_primes4] = (series4, primes)
	
def generate_primes5(limit):
	primes = []
	iterations = 0
	for i in range(2, limit + 1):
		count = 0;
		for j in primes:
			iterations = iterations + 1
			if j > int(math.sqrt(i) + 1):
				break
			if i % j == 0:
				count = count + 1
				break
		if count < 1:
			primes.append(i)
	series5.append(iterations)
	executions[generate_primes5] = (series5, primes)
	
if __name__=="__main__":
	import sys
	import os
    
	print 'Prime Numbers Plotting v', version

	max_value = 500
	

	if len(sys.argv) > 1:
		max_value = int(sys.argv[1])
	
	methods = [generate_primes0, generate_primes1, generate_primes2, generate_primes3, generate_primes4, generate_primes5]
	for i in range(2, max_value):
		for f in methods:
			f(i)
	
	import matplotlib.pyplot as plt
	import math
	plt.figure()
	x_series = range(2, max_value)
	for key in executions.keys():
		lable = key.__name__
		print '\n', lable
		f_series, f_primes = executions[key]
		plt.plot(x_series, f_series, label=lable)
		print 'series:\n', f_series
		print 'primes:\n', f_primes
	
	#plt.plot(x_series, [(x**2) for x in x_series], label="x^2")
	plt.plot(x_series, [(x**1.7) for x in x_series], label="x^1.7")
	plt.plot(x_series, [(math.log(x**700)) for x in x_series], label="log x^700")
	
	plt.legend(loc="upper left")
	plt.grid(True)
	plt.savefig("PrimesResult.png")
	print '##########################################################'
	print 'Done!'
	print 'Now check the output graph at ', os.getcwd() + '/PrimesResult.png'
	#plt.show()

