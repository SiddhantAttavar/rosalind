s = input()
t = input()
res = []
for i in range(len(s) - len(t) + 1):
	if s[i: i + len(t)] == t:
		res.append(i + 1)
print(*res)
