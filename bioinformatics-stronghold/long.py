from utils import read_fasta

l = list(read_fasta().values())

graph = [[] for _ in range(len(l))]
for i in range(len(l)):
	for j in range(len(l)):
		if i == j:
			continue

		x = min(len(l[i]), len(l[j]))
		for k in range(x, (x + 1) // 2 - 1, -1):
			if l[i][:k] == l[j][len(l[j]) - k:]:
				graph[j].append((i, k))
				break

topo = []
vis = [False] * len(graph)

def dfs(u, x):
	vis[u] = True
	for v, w in graph[u]:
		if not vis[v]:
			dfs(v, w)
	topo.append((u, x))

for i in range(len(graph)):
	if not vis[i]:
		dfs(i, 0)
topo.reverse()

res = ''
for i, x in topo:
	res += l[i][x:]
print(res)
