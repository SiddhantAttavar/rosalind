from utils import read_fasta
m = {
	'A': 'U',
	'U': 'A',
	'C': 'G',
	'G': 'C',
}
MOD = int(1e6)

s = list(read_fasta().values())[0]

dp = [[0] * len(s) for _ in range(len(s))]
for i in range(len(s) - 1):
	dp[i + 1][i] = 1

for i in range(len(s)):
	dp[i][i] = 1

for l in range(2, len(s) + 1):
	for i in range(len(s) - l + 1):
		j = i + l - 1
		dp[i][j] = dp[i + 1][j]
		if m[s[i]] == s[j]:
			dp[i][j] = (dp[i][j] + dp[i + 1][j - 1]) % MOD
		for k in range(i + 1, j):
			if m[s[i]] == s[k]:
				dp[i][j] = (dp[i][j] + dp[i + 1][k - 1] * dp[k + 1][j]) % MOD

print(dp[0][len(s) - 1])
