n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
	u, v = map(int, input().split())
	graph[u - 1].append(v - 1)
	graph[v - 1].append(u - 1)
print(*[sum(len(graph[v]) for v in graph[u]) for u in range(n)])
