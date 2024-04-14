n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
	u, v = map(int, input().split())
	graph[u - 1].append(v - 1)

vis = [False] * n
l = []
def dfs(u):
	vis[u] = True

	for v in graph[u]:
		if not vis[v]:
			dfs(v)
	
	l.append(u + 1)

for i in range(n):
	if not vis[i]:
		dfs(i)
print(*l[::-1])
