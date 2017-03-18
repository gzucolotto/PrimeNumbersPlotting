from PrimesGenerator import PrimesGenerator
import math

class PrimesGeneratorPreviousSqrt(PrimesGenerator):
	def __init__(self):
		PrimesGenerator.__init__(self)

	def __check_value__(self, value):
		"""
		Iterates through the list of previously discovered primes. If the value under test is divisible by a
		previous prime then it can't be a prime. Otherwise it is a prime number.
		The optimization of limiting the testing group up to the square root on the tested value is applied
		since any number greater then that would be a composition of the previous values.
		"""
		count = 0
		for j in self.primes:
			if j > int(math.sqrt(value) + 1):
				break
			if value % j == 0:
				count = count + 1
				if count > 1:
					break

		if count <= 1:
			return value
		return 0;