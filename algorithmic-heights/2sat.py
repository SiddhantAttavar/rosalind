from sys import setrecursionlimit
setrecursionlimit(int(1e6))
for _ in range(int(input())):
	input()
	n, m = map(int, input().split())
	graph = [[] for _ in range(2 * n)]
	rev_graph = [[] for _ in range(2 * n)]
	for _ in range(m):
		u, v = map(int, input().split())
		a = 2 * (abs(u) - 1)
		b = 2 * (abs(v) - 1)
		graph[a + (u > 0)].append(b + (v < 0))
		graph[b + (v > 0)].append(a + (u < 0))
		rev_graph[b + (v < 0)].append(a + (u > 0))
		rev_graph[a + (u < 0)].append(b + (v > 0))
	
	vis = [False] * (2 * n)
	l = []

	def dfs(u):
		vis[u] = True

		for v in graph[u]:
			if not vis[v]:
				dfs(v)
		
		l.append(u)
	
	for i in range(2 * n):
		if not vis[i]:
			dfs(i)

	c = [-1] * (2 * n)
	x = 0
	def dfs2(u, x):
		c[u] = x

		for v in rev_graph[u]:
			if c[v] == -1:
				dfs2(v, x)

	for i in l[::-1]:
		if c[i] == -1:
			dfs2(i, x)
			x += 1
	
	res = list(range(1, n + 1))
	for i in range(n):
		if c[2 * i] == c[2 * i + 1]:
			print(0)
			break
		if c[2 * i + 1] > c[2 * i]:
			res[i] *= -1
	else:
		print(1, *res)

