import PrimesGenerator as pg
import PrimesGeneratorSkip as pgs
import PrimesGeneratorHalfWay as pghw
import PrimesGeneratorSqrt as pgsqrt
import PrimesGeneratorPrevious as pgp
import PrimesGeneratorPreviousSqrt as pgpsqrt

def get_primes_generator():
	return pg.PrimesGenerator()

def get_primes_generator_skip():
	return pgs.PrimesGeneratorSkip()

def get_primes_generator_half_way():
	return pghw.PrimesGeneratorHalfWay()

def get_primes_generator_sqrt():
	return pgsqrt.PrimesGeneratorSqrt()

def get_primes_generator_previous():
	return pgp.PrimesGeneratorPrevious()

def get_primes_generator_previous_sqrt():
	return pgpsqrt.PrimesGeneratorPreviousSqrt()

generators = {
	pg: get_primes_generator(),
	pgs: get_primes_generator_skip(),
	pghw: get_primes_generator_half_way(),
	pgsqrt: get_primes_generator_sqrt(),
	pgp: get_primes_generator_previous(),
	pgpsqrt: get_primes_generator_previous_sqrt()
}

def get_generator(type):
	return generators[type]
