from sys import setrecursionlimit
from utils import revc
setrecursionlimit(int(1e9))

g = set()
while True:
	try:
		s = input()
		g.add((s[:-1], s[1:]))
		s = revc(s)
		g.add((s[:-1], s[1:]))
	except:
		break

l = []
graph = []
a = {}
for u, v in g:
	if u not in a:
		a[u] = len(l)
		l.append(u)
		graph.append([])
	
	if v not in a:
		a[v] = len(l)
		l.append(v)
		graph.append([])
	
	i = a[u]
	j = a[v]

	graph[i].append(j)
	graph[j].append(i)

cycle = []
vis = [False] * len(graph)
def dfs(u, graph, vis):
	vis[u] = True
	cycle.append(u)
	for v in graph[u]:
		if not vis[v]:
			dfs(v, graph, vis)

dfs(0, graph, vis)

res = l[0][-1]
for i in cycle[1:]:
	res += l[i][-1]
print(res)
