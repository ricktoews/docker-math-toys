from modules.mathconst import PRIMES

def tally(denom, base):
	base_factor_tally = 0
	denom_tmp = denom
	base_tmp = base
	max_non_repeat_tally = 0
	non_repeat_tally = 0
	prime_ndx = 0
	retval = 0

	current_prime = PRIMES[prime_ndx]
	while current_prime <= base_tmp:
		non_repeat_tally = 0
		base_factor_tally = 0

		# First, tally occurrences of present prime number in base's set of factors.
		while base_tmp % current_prime == 0:
			base_tmp = base_tmp / current_prime
			base_factor_tally += 1

		# If the present prime is a factor of the base, ...
		if base_factor_tally > 0:
			prime_power = current_prime**base_factor_tally

			# First, divide out all complete sets of the present prime from the denominator, and tally the number of divisions.
			while denom_tmp % prime_power == 0:
				denom_tmp /= prime_power
				non_repeat_tally += 1

			# Second, check for any remaining instances of the prime number. If there are any, divide them out, and increment the tally.
			if denom_tmp % current_prime == 0:
				non_repeat_tally += 1
				while denom_tmp % current_prime == 0:
					denom_tmp /= current_prime

			# Keep the max_non_repeat_tally up-to-date.
			max_non_repeat_tally = max(non_repeat_tally, max_non_repeat_tally)

		prime_ndx += 1
		current_prime = PRIMES[prime_ndx]

	# If denom_tmp is equal to 1 at this point, the denominator's prime factors were all included in the set of factors for the base, which means the decimal resolves.
	# If the denominator has no factors in common with the base, then there are no non-repeating digits.
	if denom_tmp == 1:
		retval = -1
	else:
		retval = max_non_repeat_tally

	return retval
