s = input()
t = input()

dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

for i in range(1, len(s) + 1):
	dp[i][0] = i
for j in range(1, len(t) + 1):
	dp[0][j] = j

for i in range(len(s)):
	for j in range(len(t)):
		dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + 1

		if s[i] == t[j]:
			dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j])

res = ''
x, y = len(s), len(t)
while x > 0 or y > 0:
	if x > 0 and y > 0 and dp[x][y] == dp[x - 1][y - 1] and s[x - 1] == t[y - 1]:
		x -= 1
		y -= 1
		res += s[x]
	elif x > 0 and dp[x][y] == dp[x - 1][y] + 1:
		x -= 1
		res += s[x]
	else:
		y -= 1
		res += t[y]

print(res[::-1])
