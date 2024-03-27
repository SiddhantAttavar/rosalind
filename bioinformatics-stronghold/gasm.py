from sys import setrecursionlimit
from utils import revc
setrecursionlimit(int(1e9))

v = []
while True:
	try:
		v.append(input())
	except:
		break

def get_graph(k):
	g = set()
	global v
	for i in v:
		for j in range(len(i) - k + 1):
			s = i[j: j + k + 1]
			g.add((s[:-1], s[1:]))
			s = revc(s)
			g.add((s[:-1], s[1:]))

	l = []
	graph = []
	rev_graph = []
	a = {}
	for u, v in g:
		if u not in a:
			a[u] = len(l)
			l.append(u)
			graph.append([])
			rev_graph.append([])
		
		if v not in a:
			a[v] = len(l)
			l.append(v)
			graph.append([])
			rev_graph.append([])
		
		i = a[u]
		j = a[v]

		graph[i].append(j)
		rev_graph[j].append(i)

	return graph, rev_graph, l

def dfs(u, graph, rev_graph, vis):
	vis[u] = True
	for v in graph[u] + rev_graph[u]:
		if not vis[v]:
			dfs(v, graph, rev_graph, vis)

cycle = []
def dfs2(u, graph, vis):
	vis[u] = True
	cycle.append(u)
	for v in graph[u]:
		if not vis[v]:
			dfs2(v, graph, vis)

for k in range(1, len(v[0])):
	graph, rev_graph, l = get_graph(k)

	comp = 0
	cycle = []
	vis = [False] * len(graph)
	for i in range(len(graph)):
		if not vis[i]:
			dfs(i, graph, rev_graph, vis)
			comp += 1
	
	if comp != 2:
		continue

	print(k)
	print(l)
	for i in graph:
		print(*i)
	
	cycle = []
	vis = [False] * len(graph)
	dfs2(0, graph, vis)

	res = l[0][-1]
	for i in cycle[1:]:
		res += l[i][-1]
	print(res)
	break
