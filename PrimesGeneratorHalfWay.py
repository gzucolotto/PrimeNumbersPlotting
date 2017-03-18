from PrimesGenerator import PrimesGenerator

class PrimesGeneratorHalfWay(PrimesGenerator):
	def __init__(self):
		PrimesGenerator.__init__(self)

	def __check_value__(self, value):
		"""
		Iterates from 1 until half way throug the value. The value being check is not devisible by any number greater than its halve.
		Tanking advantage of this property the greather halve of the iteration can be discarted.
		"""
		count = 0
		for j in range(1, (value / 2) + 1):
			if value % j == 0:
				count = count + 1
				if count > 1:
					break

		if count <= 1:
			return value
		return 0;