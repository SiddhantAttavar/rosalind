n, m = map(int, input().split())
dp = [0] * n
dp[0] = 1
dp[1] = 0
x = 1
for i in range(2, n):
	dp[i] = x - dp[i - 1]
	x += dp[i]
	if i >= m:
		x -= dp[i - m]
print(x)
