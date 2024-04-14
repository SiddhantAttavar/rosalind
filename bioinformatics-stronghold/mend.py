from utils import parse_newick

m = {
	'AA': [1, 0, 0],
	'Aa': [0, 1, 0],
	'aa': [0, 0, 1]
}

names, tree = parse_newick(input())
def dfs(u, p):
	if names[u]:
		return m[names[u]]

	res = []
	for v, w in tree[u]:
		if v == p:
			continue

		res.append(dfs(v, u))

	x, y = res
	a = [x[0] + x[1] / 2, x[1] / 2 + x[2]]
	b = [y[0] + y[1] / 2, y[1] / 2 + y[2]]
	return [
		a[0] * b[0],
		a[0] * b[1] + a[1] * b[0],
		a[1] * b[1]
	]

print(*[round(i, 3) for i in dfs(0, -1)])
