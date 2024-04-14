for _ in range(int(input())):
	input()
	n, m = map(int, input().split())
	graph = [[] for _ in range(n)]
	for _ in range(m):
		u, v = map(int, input().split())
		graph[u - 1].append(v - 1)
		graph[v - 1].append(u - 1)

	col = [0] * n
	def dfs(u, c):
		col[u] = c

		for v in graph[u]:
			if col[v] == c or (col[v] == 0 and (not dfs(v, -c))):
				return False

		return True

	for i in range(n):
		if col[i] == 0 and (not dfs(i, 1)):
			print(-1, end = ' ')
			break
	else:
		print(1, end = ' ')
