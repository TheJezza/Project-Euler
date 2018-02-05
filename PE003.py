import shelve

def compute(limit):
	factor = 2
	while factor*factor < limit:
		while limit % factor == 0:
			limit = limit / factor
		factor += 1
	return int(limit)

if __name__ == '__main__':
	print(compute(600851475143))