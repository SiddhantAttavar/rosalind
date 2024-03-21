from utils import read_fasta

s, t = read_fasta().values()

dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
for i in range(len(s)):
	for j in range(len(t)):
		dp[i + 1][j + 1] = max(
			dp[i][j + 1],
			dp[i + 1][j],
			dp[i][j] + (s[i] == t[j])
		)

res = ''
x, y = len(s), len(t)
while x > 0 and y > 0:
	if dp[x][y] == dp[x - 1][y]:
		x -= 1
	elif dp[x][y] == dp[x][y - 1]:
		y -= 1
	else:
		if s[x - 1] == t[y - 1]:
			res += s[x - 1]
		x -= 1
		y -= 1
print(res[::-1])
