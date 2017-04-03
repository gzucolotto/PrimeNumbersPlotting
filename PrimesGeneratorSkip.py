import PrimesGenerator
import StatisticCollector as st

class PrimesGeneratorSkip(PrimesGenerator.PrimesGenerator):
	def __init__(self):
		PrimesGenerator.PrimesGenerator.__init__(self)

	def __check_value__(self, value):
		"""
		Simplest implementation of a prime numbers sequence. For each value starts from the botton
		and counts how many times the value is divisible by itself. If the counting excedes 2
		the counting loop breaks.
		"""
		count = 0
		for j in range(1, value):
			# if value % j == 0:
			# 	count = count + 1
			# 	if count > 1:
			# 		break
			count = self.__iteration__(value, j, count)
			if count > 1:
				break

		if count <= 1:
			return value
		return 0

	@st.method_decorator
	def __iteration__(self, value, j, count):
		if value % j == 0:
			count = count + 1
			if count > 1:
				return count
		return count