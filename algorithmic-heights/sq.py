for _ in range(int(input())):
	input()
	n, m = map(int, input().split())
	graph = [[] for _ in range(n)]
	for _ in range(m):
		u, v = map(int, input().split())
		graph[u - 1].append(v - 1)
		graph[v - 1].append(u - 1)

	vis = [False] * n
	hist = []
	def dfs(u):
		vis[u] = True
		hist.append(u)

		for v in graph[u]:
			if not vis[v]:
				if dfs(v):
					return True
			elif len(hist) >= 4 and hist[-4] == v:
				return True

		hist.pop()
		return False

	for i in range(n):
		if vis[i]:
			continue
		if dfs(i):
			print(1, end = ' ')
			break
	else:
		print(-1, end = ' ')
