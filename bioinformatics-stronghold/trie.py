a = 'ACTG'
m = {a[i]: i for i in range(len(a))}
graph = [[-1] * 4]

while True:
	s = ''
	try:
		s = input()
	except:
		break

	u = 0
	for c in s:
		x = m[c]
		if graph[u][x] == -1:
			graph[u][x] = len(graph)
			graph.append([-1] * 4)
		u = graph[u][x]

for i in range(len(graph)):
	for j in range(4):
		if graph[i][j] != -1:
			print(i + 1, graph[i][j] + 1, a[j])
