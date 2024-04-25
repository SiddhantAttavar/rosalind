s = input()

n = len(s)
d = 'ACGT'
l = [d.index(i) for i in s]

graph = [[-1] * 4]
t = []
for i in l[::-1]:
	t.append(i)
	u = 0
	for j in t[::-1]:
		if graph[u][j] == -1:
			graph[u][j] = len(graph)
			graph.append([-1] * 4)
		u = graph[u][j]

x = 1
y = 0
for k in range(1, n + 1):
	if x <= n:
		x *= 4
	y += min(x, n - k + 1)
print((len(graph) - 1) / y)
