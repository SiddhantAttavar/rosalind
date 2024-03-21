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

a = ''
b = ''
x, y = len(s), len(t)
while x > 0 or y > 0:
	if dp[x][y] == dp[x - 1][y] + 1:
		x -= 1
		a += s[x]
		b += '-'
	elif dp[x][y] == dp[x][y - 1] + 1:
		y -= 1
		a += '-'
		b += t[y]
	else:
		x -= 1
		y -= 1
		a += s[x]
		b += t[y]

print(a[::-1])
print(b[::-1])
