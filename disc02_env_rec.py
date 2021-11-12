def multiply(m, n):
	if n <= 0:
		print("n must > 0")
	elif n == 1:
		return 1 * m
	else:
		return m + multiply(m, n - 1)

print(multiply(5, 3))

def countdown(n):
	if n == 1:
		print(n)
	else:
		countdown(n - 1)
		print(n)
countdown(10)

def sum_digits(n):
	if n // 10  == 0:
		return n
	else:
		return n % 10 + sum_digits(n // 10)

print(sum_digits(228))