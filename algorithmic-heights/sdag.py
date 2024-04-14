import sys
n, m = map(int, input().split())
graph = [{} for _ in range(n)]
for line in [input() for _ in range(m)]:
	u, v, w = map(int, line.split())
	graph[u - 1][v - 1] = w

vis = [False] * n
l = []

def dfs(u):
	vis[u] = True
	for v in graph[u]:
		if not vis[v]:
			dfs(v)
	l.append(u)

dfs(0)
d = ['x'] * n
for v in l:
	d[v] = sys.maxsize
d[0] = 0

for u in l[::-1]:
	if d[u] == sys.maxsize:
		continue

	for v in graph[u]:
		d[v] = min(d[v], d[u] + graph[u][v])

print(*d)
