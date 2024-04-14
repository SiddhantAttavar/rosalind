for _ in range(int(input())):
	input()
	n, m = map(int, input().split())
	graph = [[] for _ in range(n)]
	for _ in range(m):
		u, v = map(int, input().split())
		graph[u - 1].append(v - 1)

	a = [[False] * n for _ in range(n)]
	def dfs(u, i):
		a[i][u] = True

		for v in graph[u]:
			if not a[i][v]:
				dfs(v, i)

	for i in range(n):
		dfs(i, i)

	for i in range(n):
		for j in range(i, n):
			if not a[i][j] and not a[j][i]:
				print(-1, end = ' ')
				break
		else:
			continue
		break
	else:
		print(1, end = ' ')
