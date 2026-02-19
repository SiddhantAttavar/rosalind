from utils import read_fasta
s, t = read_fasta().values()

n = len(s)
m = len(t)

dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
	for j in range(m):
		dp[i + 1][j + 1] = max(
			dp[i][j + 1] - 1,
			dp[i + 1][j] - 1,
			dp[i][j] + (1 if s[i] == t[j] else -1)
		)


i = n - 1
j = max(range(m), key = lambda j: dp[n][j + 1])
for k in range(n):
	if dp[k + 1][m] > dp[i + 1][j + 1]:
		i = k
		j = m - 1

print(dp[i + 1][j + 1])
a = s[i + 1:][::-1]
b = '-'  * len(a)
b += t[j + 1:][::-1]
a += '-'  * (m - j - 1)

while i >= 0 and j >= 0:
	if dp[i + 1][j + 1] == dp[i][j + 1] - 1:
		a += s[i]
		b += '-'
		i -= 1
	elif dp[i + 1][j + 1] == dp[i + 1][j] - 1:
		a += '-'
		b += t[j]
		j -= 1
	else:
		assert(dp[i + 1][j + 1] == dp[i][j] + (1 if s[i] == t[j] else -1))
		a += s[i]
		b += t[j]
		i -= 1
		j -= 1

while i >= 0:
	a += s[i]
	b += '-'
	i -= 1

while j >= 0:
	a += '-'
	b += t[j]
	j -= 1

a = a[::-1]
b = b[::-1]
assert(len(a) == len(b))
assert(''.join(c for c in a if c != '-') == s)
assert(''.join(c for c in b if c != '-') == t)
print(a)
print(b)
