MOD = int(1e6)
n = int(input())
res = 1
for i in range(1, 2 * n - 1, 2):
	res = (res * i) % MOD
print(res)
