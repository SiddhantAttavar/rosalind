from utils import parse_newick

names, tree = parse_newick(input())

def dfs2(u, p, res):
	if names[u]:
		res[names[u]] = True

	for v, w in tree[u]:
		if v != p:
			dfs2(v, u, res)

def dfs(u, p):
	for v, w in tree[u]:
		if v == p:
			continue

		res = {s: False for s in names if s}
		dfs(v, u)

		if names[v] == '':
			dfs2(v, u, res)
			l = list(res.items())
			l.sort(key = lambda x: x[0])
			print(*[int(x[1]) for x in l], sep = '')

dfs(0, -1)
