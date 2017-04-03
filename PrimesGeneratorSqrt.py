from PrimesGenerator import PrimesGenerator
import math
import StatisticCollector as st

class PrimesGeneratorSqrt(PrimesGenerator):
	def __init__(self):
		PrimesGenerator.__init__(self)

	def __check_value__(self, value):
		"""
		Iterates from 1 until up to the square root of the value being checked. Any number greater then the square
		root of the value would be a composition of the previous already tested numbers. Going further would
		be, in essence, a repetition of a previous check.
		"""
		count = 0
		for j in range(1, int(math.sqrt(value) + 1)):
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