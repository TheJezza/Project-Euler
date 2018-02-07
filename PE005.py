def compute():
	n = 20
	while True:
		for i in range(1, 21):
			#print('\tchecking if ' + str(n) + '%' + str(i) + ' == 0')
			if n % i != 0:
				#print('\tnope')
				break
			if i == 20:
				return n
		n += 20


if __name__ == '__main__':
	print(compute())