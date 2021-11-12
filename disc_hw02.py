def square(x):
	return x * x

def so_slow(num):
	x = num
	while x > 0:
		x = x + 1
	return x / 0

def is_prime(n):
	i = 2
	while i < n:
		if n % i == 0:
			return False
		i += 1
	return True

print(is_prime(10))
print(is_prime(7))

print(7 % 6)

def keep_ints(cond, n):
	i = 1
	while i <= n:
		if cond(i):
			print(i)
		i += 1
def is_even(x):
	return x % 2 == 0

keep_ints(is_even, 5)

def outer(x):
	def inner(y):
		print(y)
	return inner

def outer_other(x):
	return inner

# def inner(y):

# 这两个函数的区别是 环境不同 在外部定义的inner不能获取outer内部的变量

def q_outer(n):
	def q_inner(m):
		return n - m
	return q_inner

f = q_outer(10)
f(4)
q_outer(5)(4)

def keep_ints_one_arg(n):
	def condition(cond):
		i = 1
		while i <= n:
			if cond(i):
				print(i)
			i += 1
	return condition

keep_ints_one_arg(5)(is_even)




















