for _ in range(int(input())):
	input()
	n, m = map(int, input().split())
	graph = [[] for _ in range(n)]
	a = [set() for _ in range(n)]
	for _ in range(m):
		u, v = map(int, input().split())
		graph[u - 1].append(v - 1)
		a[u - 1].add(v - 1)

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
	
	l.reverse()
	for i in range(n - 1):
		if l[i + 1] not in a[l[i]]:
			print(-1)
			break
	else:
		print(1, *[i + 1 for i in l])
