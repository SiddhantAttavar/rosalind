from sys import setrecursionlimit
from utils import revc
setrecursionlimit(int(1e9))

p = []
while True:
	try:
		p.append(input())
	except:
		break

p += [revc(s) for s in p]

res = '_' * int(1e6)
for k in range(len(p[0]) - 1, 0, -1):
	a = {}
	l = []
	e = []
	for s in p:
		for i in range(len(s) - k):
			u = s[i: i + k]
			v = s[i + 1: i + k + 1]
			if u not in a:
				a[u] = len(a)
				l.append(u)
			if v not in a:
				a[v] = len(a)
				l.append(v)
			e.append((a[u], a[v]))

	graph = dict(e)
	s = ''
	u = next(iter(graph))
	v = u
	while u in graph:
		s += l[u][-1]
		u = graph.pop(u)

	if u == v:
		print(s)
		exit(0)
