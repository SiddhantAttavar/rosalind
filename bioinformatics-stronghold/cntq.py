from functools import cache
from sys import setrecursionlimit
setrecursionlimit(int(1e6))
MOD = int(1e6)
n = int(input())

@cache
def nCr(n, r):
	if r == 0 or r == n:
		return 1

	return (nCr(n - 1, r - 1) + nCr(n - 1, r)) % MOD

print(nCr(n, 4))
