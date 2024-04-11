s = input()

l = []
while True:
	try:
		l.append(input())
	except:
		break

def solve(s, a, b):
	dp = [[False] * (len(b) + 1) for _ in range(len(a) + 1)]
	dp[0][0] = True

	for i in range(len(a)):
		dp[i + 1][0] = dp[i][0] and s[i] == a[i]
	for j in range(len(b)):
		dp[0][j + 1] = dp[0][j] and s[j] == b[j]

	for i in range(len(a)):
		for j in range(len(b)):
			dp[i + 1][j + 1] = (
				(dp[i][j + 1] and s[i + j + 1] == a[i]) or
				(dp[i + 1][j] and s[i + j + 1] == b[j])
			)
	return dp[len(a)][len(b)]

def check(s, a, b):
	for i in range(len(s) - len(a) - len(b) + 1):
		if solve(s[i: i + len(a) + len(b)], a, b):
			return True
	return False

res = [[True] * len(l) for _ in range(len(l))]
for i in range(len(l)):
	for j in range(i + 1):
		res[i][j] = res[j][i] = check(s, l[i], l[j])

for i in res:
	print(*map(int, i))
