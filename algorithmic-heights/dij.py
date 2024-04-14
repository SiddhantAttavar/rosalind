from queue import PriorityQueue
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
	u, v, w = map(int, input().split())
	graph[u - 1].append((v - 1, w))

d = [int(1e9)] * n
pq = PriorityQueue()
pq.put((0, 0))
d[0] = 0
while not pq.empty():
	x, u = pq.get()

	for v, w in graph[u]:
		if d[u] + w < d[v]:
			d[v] = d[u] + w
			pq.put((d[v], v))
for i in range(n):
	if d[i] == int(1e9):
		d[i] = -1
print(*d)
