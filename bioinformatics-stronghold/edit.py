from utils import read_fasta

s, t = read_fasta().values()

dp = [[int(1e9)] * (len(t) + 1) for _ in range(len(s) + 1)]
dp[0][0] = 0
for i in range(len(s)):
	for j in range(len(t)):
		dp[i + 1][j + 1] = min(
			dp[i][j + 1] + 1,
			dp[i + 1][j] + 1,
			dp[i][j] + (s[i] != t[j])
		)

print(dp[len(s)][len(t)])
