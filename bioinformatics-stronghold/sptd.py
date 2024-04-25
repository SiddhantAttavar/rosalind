from utils import parse_newick
l = input().split()
d = {l[i]: i for i in range(len(l))}

a, x = parse_newick(input())
b, y = parse_newick(input())
a = [d[i] if i else -1 for i in a]
b = [d[i] if i else -1 for i in b]

def dfs(u, p, names, graph, splits):
	if len(graph[u]) == 1:
		return [names[u]]

	res = []
	for v, w in graph[u]:
		if v != p:
			res += dfs(v, u, names, graph, splits)
	
	if len(res) >= 2 and len(res) <= len(l) - 2:
		splits.append(tuple(sorted(res)))
	return res

p = []
dfs(0, -1, a, x, p)

q = []
dfs(0, -1, b, y, q)

r = set(p + q)
print(2 * len(r) - (len(p) + len(q)))
