def compute(limit):
	sum_of_squares = sum([i**2 for i in range(1, limit + 1)])
	square_of_sum = sum(range(1, limit + 1))**2
	return square_of_sum - sum_of_squares

if __name__ == '__main__':
	print(compute(100))