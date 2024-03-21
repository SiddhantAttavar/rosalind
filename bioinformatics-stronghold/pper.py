n, k = map(int, input().split())
res = 1
MOD = int(1e6)
for i in range(n - k + 1, n + 1):
	res = (res * i) % MOD
print(res)
