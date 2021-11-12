def sum_cubes(n):
	total, k = 0, 1
	while k <= n:
		total, k = total + k * k * k, k + 1
	return total

def sum_naturals(n):
	total, k = 0, 1
	while k<= n:
		total, k = total + k, k + 1
	return total

# 上面两个函数中，共同的部分可以被抽象成一个函数

def summations(n, term):
	total, k = 0, 1
	while k <= n:
		total, k = total + term(k), k + 1
	return total

def cube(x):
	return x * x * x

# 把summations函数当作一个Process函数
def sum_cubes_higher_order(n):
	return summations(n, cube)

def naturals(x):
	return x


def sum_naturals_higher_order(n):
	return summations(n, naturals)

result = sum_cubes_higher_order(3)
print(result)


def improve(update, close, guess = 1):
	while not close(guess):
		guess = update(guess)
	return guess

def golden_update(guess):
	return 1/guess + 1

def square_close_to_successor(guess):
	return approx_eq(guess * guess, guess + 1)

def approx_eq(x, y, tolerance=1e-15):
	return abs(x - y) < tolerance

phi = 1/2 + sqrt(5)/2

def improve_test():
	approx_phi = improve(golden_update, square_close_to_successor)
	assert approx_eq(phi, approx_phi), ""

















