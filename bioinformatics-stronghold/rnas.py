m = {
	'A': 'U',
	'U': 'AG',
	'C': 'G',
	'G': 'CU',
}

s = input()

dp = [[0] * len(s) for _ in range(len(s))]
for i in range(len(s) - 1):
	dp[i + 1][i] = 1

for i in range(len(s)):
	dp[i][i] = 1

for l in range(2, len(s) + 1):
	for i in range(len(s) - l + 1):
		j = i + l - 1
		dp[i][j] = dp[i + 1][j]
		if l >= 5 and s[j] in m[s[i]]:
			dp[i][j] = dp[i][j] + dp[i + 1][j - 1]
		for k in range(i + 4, j):
			if s[k] in m[s[i]]:
				dp[i][j] = dp[i][j] + dp[i + 1][k - 1] * dp[k + 1][j]

print(dp[0][len(s) - 1])
