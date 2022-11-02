#! /usr/local/bin/python

import sys
import math
sys.path.insert(1, '..')

from utils.mathutils import is_relative_prime

def get_pythag_by_corner(param_corner):
	corner = int(param_corner)
	squares = []
	i = 1
	circuit_breaker = 500
	while len(squares) <= 100 and circuit_breaker > 0:
		test = corner * (corner + 2 * i)
		sqrt = int(math.sqrt(test))
		print("test %d, sqrt %d" % (test, sqrt))
		if sqrt * sqrt == test:
			circuit_breaker = circuit_breaker - 1
			is_primitive = is_relative_prime(corner, i)
			a = int(math.sqrt(test))
			b = i
			c = int(math.sqrt(test + b * b))
			squares.append( { "a": a, "b": b, "c": c, "is_primitive": is_primitive } )
		i = i + 1

	return squares


# Imagine a c x c square. The outer layer is c + (c-1). The next is (c-1)+(c-2), and so on.
# This function inspects sums of layers, from the outer inward; and it gathers sums that
# are square.
def find_layers(c):
	result = []
	layer_sum = 0
	layer = c * 2 - 1
	while layer > 5:
		layer_sum = layer_sum + layer
		sq_root = math.sqrt(layer_sum)
		if sq_root.is_integer():
			result.append(layer_sum)
		layer = layer - 2

	return result


def get_triples(c_list):
	data = []
	for num in c_list:
		a_squares = find_layers(num)
		triples = []
		if len(a_squares) > 0:
			triples = []
			used = []
			n = 1
			primes = 0
			for a_square in a_squares:
				a = int(math.sqrt(a_square))
				c = num
				b = int(math.sqrt(num**2 - a_square))
				if not a in used and not b in used:
					triple = { "a": a, "b": b, "c": c }
					if is_relative_prime(a, b):
						primes = primes + 1
						triples.append({ "a": a, "b": b, "c": c, "prime": True })
					else:			
						triples.append({ "a": a, "b": b, "c": c, "prime": False })
				used.append(a)
				used.append(b)
				n = n + 1
		data.append({ "num": num, "a_squares": a_squares, "triples": triples })

	return data


