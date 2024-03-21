from utils import read_fasta

m = {
	'A': 'T',
	'T': 'A',
	'C': 'G',
	'G': 'C',
}

s = list(read_fasta().values())[0]
dp = [[False] * len(s) for _ in range(len(s))]

for i in range(len(s) - 1):
	dp[i][i + 1] = m[s[i]] == s[i + 1]

for l in range(4, 14, 2):
	for i in range(len(s) - l + 1):
		if m[s[i]] == s[i + l - 1] and dp[i + 1][i + l - 2]:
			dp[i][i + l - 1] = True
			print(i + 1, l)
