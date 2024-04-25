from utils import read_fasta

s, t = read_fasta().values()

dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
for i in range(len(s)):
	dp[i + 1][0] = -2 * (i + 1)
for j in range(len(t)):
	dp[0][j + 1] = -2 * (j + 1)

for i in range(len(s)):
	for j in range(len(t)):
		dp[i + 1][j + 1] = max(
			dp[i][j + 1] - 2,
			dp[i + 1][j] - 2,
			dp[i][j] + (1 if s[len(s) - i - 1] == t[j] else -2),
		)

x, y = 0, 0
for i in range(len(s) + 1):
	for j in range(len(t) + 1):
		if dp[x][y] < dp[i][j]:
			x, y = i, j

print(dp[x][y])

a = ''
b = ''
while x > 0 or y > 0:
	if x > 0 and dp[x][y] == dp[x - 1][y] - 2:
		x -= 1
		a += s[x]
		b += '-'
	elif y > 0 and dp[x][y] == dp[x][y - 1] - 2:
		y -= 1
		a += '-'
		b += t[y]
	else:
		x -= 1
		y -= 1
		# print(x, len(s))
		a += s[x]
		b += t[y]

print(a)
print(b[::-1])
