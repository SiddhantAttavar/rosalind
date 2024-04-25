from utils import parse_newick
l = input().split()
d = {l[i]: i for i in range(len(l))}

a, x = parse_newick(input())
b, y = parse_newick(input())
a = [d[i] if i else -1 for i in a]
b = [d[i] if i else -1 for i in b]

def dfs(u, p, s, graph, q):
	if len(graph[u]) == 1:
		return [s[u]]

	res = []
	for v, w in graph[u]:
		if v != p:
			res.append(dfs(v, u, s, graph, q))
	
	for i in range(len(res)):
		for j in range(i):
			gen_quartets(res[j], res[i], q)

	l = []
	for i in res:
		l += i
	return sorted(l)

p = []
dfs(0, -1, a, x, p)

q = []
dfs(0, -1, b, y, q)

r = set(p + q)
print(2 * len(r) - (len(p) + len(q)))
