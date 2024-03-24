from math import factorial

n, m = map(int, input().split())
c = factorial(n) // factorial(m) // factorial(n - m)
res = c
for i in range(m + 1, n + 1):
	c = (c * (n - i + 1)) // i
	res += c
print(res % int(1e6))
