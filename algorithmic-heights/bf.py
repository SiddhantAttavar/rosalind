n, m = map(int, input().split())
e = []
for _ in range(m):
	u, v, w = map(int, input().split())
	e.append((u - 1, v - 1, w))

d = [-1] * n
d[0] = 0
for i in range(n - 1):
	for u, v, w in e:
		if d[u] != -1 and (d[v] == -1 or d[v] > d[u] + w):
			d[v] = d[u] + w

for i in range(n):
	if d[i] == -1:
		d[i] = 'x'
print(*d)
