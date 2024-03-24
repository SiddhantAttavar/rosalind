from itertools import permutations
n = int(input())
res = []
for l in permutations(range(1, n + 1)):
	for i in range(1 << n):
		res.append([l[j] if i & (1 << j) else -l[j] for j in range(n)])

print(len(res))
for i in res:
	print(*i)
