from functools import cache
from math import log10

n, m = map(int, input().split())
t = n * 2
q = 1 / pow(t, t)

@cache
def nCr(n, r):
	if r == 0 or r == n:
		return 1
	return nCr(n - 1, r - 1) + nCr(n - 1, r)

a = list(map(int, input().split()))

@cache
def solve(x, y, j):
	if x == 0:
		return y == t - a[j]

	res = 0
	for i in range(t + 1):
		res += solve(x - 1, i, j) * pow(i, y) * pow(t - i, t - y)
	return res * nCr(t, y) * q

for i in range(m):
	print(*[log10(solve(i + 1, t, j)) for j in range(len(a))])
