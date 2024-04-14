n, m = map(int, input().split())
graph = [[] for _ in range(n)]
rev_graph = [[] for _ in range(n)]
for _ in range(m):
	u, v = map(int, input().split())
	graph[u - 1].append(v - 1)
	rev_graph[v - 1].append(u - 1)

def dfs(graph, vis, u):
	vis[u] = True

	for v in graph[u]:
		if not vis[v]:
			dfs(graph, vis, v)

res = 0
x = [-1] * n
for i in range(n):
	if x[i] != -1:
		continue

	vis = [False] * n
	rev_vis = [False] * n
	dfs(graph, vis, i)
	dfs(rev_graph, rev_vis, i)
	for j in range(n):
		if vis[j] and rev_vis[j]:
			x[j] = i
	res += 1
print(res)