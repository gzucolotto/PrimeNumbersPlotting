class PrimesGenerator:
	"""
	Generates a series of prime numbers.
	"""
	primes = [1]

	def __init__(self):
		self.primes = [1]

	def generate_series(self, limit):
		self.primes = [1]
		for i in range(2, limit + 1):
			candidate = self.__check_value__(i)
			if candidate > 0:
				self.primes.append(candidate)
		return self.primes

	def __check_value__(self, value):
		"""
		Simplest implementation of a prime numbers sequence. For each value starts from the botton
		and counts how many times the value is divisible by itself.
		"""
		count = 0
		for j in range(1, value):
			if value % j == 0:
				count = count + 1
		if count <= 1:
			return value
		return 0;
