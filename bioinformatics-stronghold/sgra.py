m = {
	'A': 71.03711,
	'C': 103.00919,
	'D': 115.02694,
	'E': 129.04259,
	'F': 147.06841,
	'G': 57.02146,
	'H': 137.05891,
	'I': 113.08406,
	'K': 128.09496,
	'L': 113.08406,
	'M': 131.04049,
	'N': 114.04293,
	'P': 97.05276,
	'Q': 128.05858,
	'R': 156.10111,
	'S': 87.03203,
	'T': 101.04768,
	'V': 99.06841,
	'W': 186.07931,
	'Y': 163.06333 ,
}

l = []
while True:
	try:
		l.append(float(input()))
	except:
		break
l.sort()

d = {round(v, 2): k for k, v in m.items()}

graph = [[] for _ in range(len(l))]
for i in range(len(l)):
	for j in range(i):
		x = round(l[i] - l[j], 2)
		c = d.get(x, '')
		if c:
			graph[i].append((j, c))


vis = [False] * len(l)
t = []
def dfs(u):
	vis[u] = True
	for v, w in graph[u]:
		if not vis[v]:
			dfs(v)
	t.append(u)
t.reverse()

for i in range(len(l)):
	if not vis[i]:
		dfs(i)

dp = [0] * len(l)
p = [(-1, '')] * len(l)
for u in t:
	for v, w in graph[u]:
		if dp[v] < dp[u] + 1:
			dp[v] = dp[u] + 1
			p[v] = (u, w)

u = max(t, key = lambda x: dp[x])

s = ''
while u != -1:
	s += p[u][1]
	u = p[u][0]

print(s)
