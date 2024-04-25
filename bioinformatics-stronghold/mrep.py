from functools import cache
s = input()

@cache
def solve(i, j):
	if j == len(s) or s[i] != s[j]:
		return 0

	return solve(i + 1, j + 1) + 1

res = set()
for i in range(len(s)):
	for j in range(i + 1, len(s)):
		if (i == 0 or solve(i - 1, j - 1) == 0) and solve(i, j) >= 20:
			res.add(s[i: i + solve(i, j)])
print(*res, sep = '\n')
