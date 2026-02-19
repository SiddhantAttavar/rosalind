from utils import read_fasta

s, t = read_fasta().values()

dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
for j in range(1, len(t)):
	dp[0][j + 1] = -2 * j

for i in range(len(s)):
	for j in range(len(t)):
		dp[i + 1][j + 1] = max(
			dp[i][j + 1] - 2,
			dp[i + 1][j] - 2,
			dp[i][j] + (1 if s[i] == t[j] else -2),
		)

x = len(s) - 1
y = max(range(len(t)), key = lambda y: dp[len(s)][y + 1])
print(dp[x + 1][y + 1])

a = ''
b = ''
while x >= 0 and y >= 0:
	if dp[x + 1][y + 1] == dp[x][y + 1] - 2:
		a += s[x]
		b += '-'
		x -= 1
	elif dp[x + 1][y + 1] == dp[x + 1][y] - 2:
		a += '-'
		b += t[y]
		y -= 1
	else:
		a += s[x]
		b += t[y]
		x -= 1
		y -= 1

while y >= 0:
	a += '-'
	b += t[y]
	y -= 1

print(a[::-1])
print(b[::-1])
