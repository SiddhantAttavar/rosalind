from math import factorial
k, n = map(int, input().split())
x = 1 << k
c = factorial(x) // factorial(n) // factorial(x - n)
y = 3 ** (x - n)
res = c * y
for i in range(n + 1, x + 1):
	y /= 3
	c = (c * (x - i + 1)) // i
	res += c * y
y = res / (1 << (2 * x))
print(y)
