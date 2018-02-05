def compute():
	palindromes = []
	start = x = y = 999
	itr = 1
	while x > 99:
		while y > 99:
			product = x * y
			print('product = ' + str(x) + ' * ' + str(y) + ' = ' + str(x*y))
			if [int(i) for i in str(product)] == [int(i) for i in str(product)][::-1]:
				palindromes.append(product)
			y -= 1
		# product = x * y
		# print('product = ' + str(x) + ' * ' + str(y) + ' = ' + str(x*y))
		# if [int(i) for i in str(product)] == [int(i) for i in str(product)][::-1]:
		# 	return product
		x -= 1
		itr += 1
		y = start - itr
	return max(palindromes)


if __name__ == '__main__':
	print(compute())