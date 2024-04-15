s = input()
k = int(input())
a = {}
e = []
while True:
	try:
		p, v, i, l = input().split()
		if p not in a:
			a[p] = len(a)
		if v not in a:
			a[v] = len(a)
		e.append((a[p], a[v], int(i) - 1, int(l)))
	except:
		break

d = [0] * len(a)
graph = [[] for _ in range(len(a))]
for u, v, i, l in e:
	graph[u].append((v, i, l))
	d[v] += 1

f = [0] * len(a)
res = ''
def dfs(u, p, t):
	global res
	f[u] = len(graph[u]) == 0
	for v, i, l in graph[u]:
		if v != p:
			f[u] += dfs(v, u, t + s[i: i + l])
	if f[u] >= k and len(t) > len(res):
		res = t
	return f[u]

dfs(d.index(0), -1, '')
print(res)
