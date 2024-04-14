from sys import setrecursionlimit
setrecursionlimit(int(1e6))
for _ in range(int(input())):
	input()
	n, m = map(int, input().split())
	graph = [[] for _ in range(n)]
	rev_graph = [[] for _ in range(n)]
	for _ in range(m):
		u, v = map(int, input().split())
		graph[u - 1].append(v - 1)
		rev_graph[v - 1].append(u - 1)
	
	vis = [False] * n
	l = []

	def dfs(u):
		vis[u] = True

		for v in graph[u]:
			if not vis[v]:
				dfs(v)
		
		l.append(u)
	
	for i in range(n):
		if not vis[i]:
			dfs(i)
	vis = [False] * n

	def dfs2(u):
		vis[u] = True
	
		for v in graph[u]:
			if not vis[v]:
				dfs2(v)
	
	dfs2(l[-1])

	if vis == [True] * n:
		print(l[-1] + 1, end = ' ')
	else:
		print(-1, end = ' ')
