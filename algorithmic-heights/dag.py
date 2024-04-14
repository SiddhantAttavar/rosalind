for _ in range(int(input())):
	input()
	n, m = map(int, input().split())
	graph = [[] for _ in range(n)]
	for _ in range(m):
		u, v = map(int, input().split())
		graph[u - 1].append(v - 1)

	vis = [False] * n
	in_stack = [False] * n
	def dfs(u):
		vis[u] = True
		in_stack[u] = True

		for v in graph[u]:
			if not vis[v]:
				if dfs(v):
					return True
			elif in_stack[v]:
				return True

		in_stack[u] = False
		return False

	for i in range(n):
		if vis[i]:
			continue
		if dfs(i):
			print(-1, end = ' ')
			break
	else:
		print(1, end = ' ')
