#!/usr/bin/python

import unittest2 as unittest
import PrimesGenerator as pg
import PrimesGeneratorSkip as pgs
import PrimesGeneratorHalfWay as pghw
import PrimesGeneratorSqrt as pgsqrt
import PrimesGeneratorPrevious as pgp
import PrimesGeneratorPreviousSqrt as pgpsqrt
import PrimesGeneratorBuilder as builder
import StatisticCollector as st

class DecoratorTarget:
	@st.method_decorator
	def some_method(self):
		print "in some_method"

	@st.method_decorator
	def some_other_method(self):
		print "in some_other_method"

class MinimumFunctionalityTest(unittest.TestCase):

	def setUp(self):
		#print "----invoking setup-----", st.counter.__len__()
		st.reset_counters()
		#print "----should be 0-----", st.counter.__len__()

	def test_decorator(self):
		dt = DecoratorTarget()
		dt.some_method()
		dt.some_method()
		count = st.counter.__len__()
		# print "dt.some_method", dt.some_method
		# print "dt.some_other_method", dt.some_other_method

		self.assertEquals(count, 1)
		self.assertEquals(st.counter.items()[0][1], 2)

	def test_decorator_clear(self):
		dt = DecoratorTarget()
		dt.some_method()
		dt.some_method()
		self.assertEquals(st.counter.__len__(), 1)
		self.assertEquals(st.times.__len__(), 1)
		self.assertEquals(st.lables.__len__(), 1)

		st.reset_counters()
		self.assertEquals(st.counter.__len__(), 0)
		self.assertEquals(st.times.__len__(), 0)
		self.assertEquals(st.lables.__len__(), 0)


	def __minimum_sequence_check__(self, generator):
		result = generator.generate_series(3)
		self.assertEquals(result, [1, 2, 3])

	def test_prime_sequence(self):
		self.__minimum_sequence_check__(builder.get_generator(pg))

	def test_prime_sequence_decorator(self):
		self.__minimum_sequence_check__(builder.get_generator(pg))
		self.assertEquals(st.counter.__len__(), 1)
		key = list(st.counter.keys())[0]
		self.assertEquals(st.lables[key], "PrimesGenerator")

	def test_prime_sequence_skip(self):
		self.__minimum_sequence_check__(builder.get_generator(pgs))

	def test_prime_sequence_half_way(self):
		self.__minimum_sequence_check__(builder.get_generator(pghw))

	def test_prime_sequence_sqrt(self):
		self.__minimum_sequence_check__(builder.get_generator(pgsqrt))

	def test_prime_sequence_previous(self):
		self.__minimum_sequence_check__(builder.get_generator(pgp))

	def test_prime_sequence_previous_sqrt(self):
		self.__minimum_sequence_check__(builder.get_generator(pgpsqrt))

	def test_generatos_builder_responces_by_class(self):
		self.assertTrue(isinstance(builder.get_generator(pg),  pg.PrimesGenerator))
		self.assertTrue(isinstance(builder.get_generator(pgs),  pgs.PrimesGeneratorSkip))
		self.assertTrue(isinstance(builder.get_generator(pghw),  pghw.PrimesGeneratorHalfWay))
		self.assertTrue(isinstance(builder.get_generator(pgsqrt),  pgsqrt.PrimesGeneratorSqrt))
		self.assertTrue(isinstance(builder.get_generator(pgp),  pgp.PrimesGeneratorPrevious))
		self.assertTrue(isinstance(builder.get_generator(pgpsqrt),  pgpsqrt.PrimesGeneratorPreviousSqrt))

	def test_implementations_integrity_up_1000(self):
		limit = 1000
		series0 = builder.get_generator(pg).generate_series(limit)
		series1 = builder.get_generator(pgs).generate_series(limit)
		series2 = builder.get_generator(pghw).generate_series(limit)
		series3 = builder.get_generator(pgsqrt).generate_series(limit)
		series4 = builder.get_generator(pgp).generate_series(limit)
		series5 = builder.get_generator(pgpsqrt).generate_series(limit)

		self.assertEquals(series0, series1)
		self.assertEquals(series0, series2)
		self.assertEquals(series0, series3)
		self.assertEquals(series0, series4)
		self.assertEquals(series0, series5)

		# for key, value in st.counter.iteritems():
		# 	#print "key:", key, "key.name:", key.__name__, "value:", value, "class:", key.func_name
		# 	print "key:", key, "value:", value

	

if __name__ == '__main__':
    unittest.main()
