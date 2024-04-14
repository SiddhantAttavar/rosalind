n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
	u, v = map(int, input().split())
	graph[u - 1].append(v - 1)
	graph[v - 1].append(u - 1)

vis = [False] * n
def dfs(u):
	vis[u] = True

	for v in graph[u]:
		if not vis[v]:
			dfs(v)

res = 0
for i in range(n):
	if not vis[i]:
		res += 1
		dfs(i)

print(res)
