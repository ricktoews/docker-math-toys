SQRT_5 = 5**.5
PHI = (SQRT_5 + 1) / 2

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 183, 191, 193, 199]

def is_relative_prime(a, b):
	[a, b] = [min(a, b), max(a, b)]
	while a > 1:
		[a, b] = [min(b%a, a), max(b%a, a)]

	return a == 1

def is_prime(p):
	_result = True
	for prime in PRIMES:
		if prime*prime > p:
			break

		if p % prime == 0:
			_result = False
			break
	return _result



