from utils import read_fasta

MOD = (1 << 27) - 1
s, t = read_fasta().values()

dp = [[int(1e9)] * (len(t) + 1) for _ in range(len(s) + 1)]
a = [[1] * (len(t) + 1) for _ in range(len(s) + 1)]
dp[0][0] = 0
for i in range(len(s)):
	dp[i + 1][0] = i + 1
for j in range(len(t)):
	dp[0][j + 1] = j + 1
for i in range(len(s)):
	for j in range(len(t)):
		dp[i + 1][j + 1] = min(
			dp[i][j + 1] + 1,
			dp[i + 1][j] + 1,
			dp[i][j] + (s[i] != t[j])
		)

		a[i + 1][j + 1] = (
			a[i][j + 1] * (dp[i + 1][j + 1] == (dp[i][j + 1] + 1)) + 
			a[i + 1][j] * (dp[i + 1][j + 1] == (dp[i + 1][j] + 1)) + 
			a[i][j] * (dp[i + 1][j + 1] == (dp[i][j] + (s[i] != t[j])))
		) % MOD

print(a[len(s)][len(t)])
