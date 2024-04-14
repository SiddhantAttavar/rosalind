from queue import PriorityQueue
for _ in range(int(input())):
	# input()
	n, m = map(int, input().split())
	graph = [[] for _ in range(n)]
	a, b, c = map(int, input().split())
	for _ in range(m - 1):
		u, v, w = map(int, input().split())
		graph[u - 1].append((v - 1, w))

	pq = PriorityQueue()
	d = [int(1e9)] * n
	d[b - 1] = 0
	pq.put((0, b - 1))
	while not pq.empty():
		x, u = pq.get()
		
		for v, w in graph[u]:
			if d[v] == int(1e9) or d[v] > d[u] + w:
				d[v] = d[u] + w
				pq.put((d[v], v))

	if d[a - 1] == int(1e9):
		print(-1, end = ' ')
	else:
		print(d[a - 1] + c, end = ' ')
