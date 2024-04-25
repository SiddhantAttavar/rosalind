from functools import cache

n, m, g, k = map(int, input().split())
t = n * 2
q = 1 / pow(t, t)

@cache
def nCr(n, r):
	if r == 0 or r == n:
		return 1
	return nCr(n - 1, r - 1) + nCr(n - 1, r)

@cache
def solve(x, y):
	if x == 0:
		return y == m

	res = 0
	for i in range(t + 1):
		res += solve(x - 1, i) * pow(i, y) * pow(t - i, t - y)
	return res * nCr(t, y) * q

res = 0
for i in range(t - k + 1):
	res += solve(g, i)
print(f'{res:.3f}')
