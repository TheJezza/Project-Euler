def compute(limit):
	factors = primes(limit)
	#for p in primes:
	for f in factors:
		if factors[f]==True and (limit%f) != 0:
			factors[f] = False
	return max([i for i in factors if factors[i]==True])

def primes(limit):
	limitn = limit + 1
	primes = dict()
	for i in range(2, limitn):
		primes[i] = True

	for p in primes:
		factors = range(p, limitn, p)
		for f in factors[1:]:
			primes[f] = False
	return primes
	#return [i for i in primes if primes[i]==True]

if __name__ == '__main__':
  print(compute(536))