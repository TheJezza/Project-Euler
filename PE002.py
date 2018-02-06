def compute():
  total = 0
  n = 0
  while fib(n) < 4000000:
  	if fib(n) % 2 == 0:
  	  total += fib(n)
  	n += 1
  return total

def fib(n, computed = {0: 0, 1: 1}):
	if n not in computed:
		computed[n] = fib(n-1, computed) + fib(n-2, computed)
	return computed[n]

if __name__ == '__main__':
  print(compute())