from utils import parse_newick

def dfs(u, p, y, tree):
	if u == y:
		return 0
	for v, w in tree[u]:
		if v != p:
			x = dfs(v, u, y, tree)
			if x != -1:
				return x + w
	return -1

while True:
	try:
		s = input()
		a, b = input().split()
	except:
		break

	names, trees = parse_newick(s)
	print(dfs(names.index(a), -1, names.index(b), trees), end = ' ')

	try:
		input()
	except:
		break
