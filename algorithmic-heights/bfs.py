from queue import Queue
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
	u, v = map(int, input().split())
	graph[u - 1].append(v - 1)

d = [-1] * n
q = Queue()
q.put(0)
d[0] = 0
while not q.empty():
	u = q.get()

	for v in graph[u]:
		if d[v] == -1:
			d[v] = d[u] + 1
			q.put(v)
print(*d)
