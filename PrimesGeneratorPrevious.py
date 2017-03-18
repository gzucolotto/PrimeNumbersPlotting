from PrimesGenerator import PrimesGenerator

class PrimesGeneratorPrevious(PrimesGenerator):
	def __init__(self):
		PrimesGenerator.__init__(self)

	def __check_value__(self, value):
		"""
		Iterates through the list of previously discovered primes. If the value under test is divisible by a
		previous prime then it can't be a prime. Otherwise it is a prime number
		"""
		count = 0
		for j in self.primes:
			if value % j == 0:
				count = count + 1
				if count > 1:
					break

		if count <= 1:
			return value
		return 0;