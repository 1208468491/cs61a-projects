def sum_digits(n):
	if n // 10 != 0:
		all_but_last, last = n % 10, last // 10
		return sum_digits(all_but_last) + last
	else:
		return n
def fact_iter(n):
	total, k = 1, 1
	while k <= n:
		total, k = total * k, k + 1
	return total

def fact_iter_recur(n):
	if n != 1:
		return n * fact_iter_recur(n-1)
	else:
		return 1

def is_even(n):
	if (n == 0):
		return True
	else:
		return is_odd(n - 1)

def is_odd(n):
	if (n == 0):
		return False
	else:
		return is_even(n - 1)

def is_even(n):
	if n == 0:
		return True
	else:
		if (n - 1) == 0:
			return False
		else:
			return is_even((n - 1) - 1)

def cascade(n):
	"""Print a cascade of prefixes of n."""
	if n < 10:
		print(n)
	else:
		print(n)
		cascade(n / 10)
		print(n)

def cascade_simple(n):
	print(n)
	if n >= 10:
		cascade_simples(n // 10)
		print(n)


def play_alice(n):
	if n - 1 == 0:
		return "alice"
	else:
		play_bob( n - 1)


def play_bob(n):
	if n - 1 == 0:
		print("bob")
	elif is_even(n):
		play_alice(n - 2)
	else:
		play_alice(n - 1)

def fib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fib(n - 2) + fib(n - 1)



















