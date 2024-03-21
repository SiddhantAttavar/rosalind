n = int(input())
graph = [[] for _ in range(n)]

while True:
	try:
		u, v = map(int, input().split())
		graph[u - 1].append(v - 1)
		graph[v - 1].append(u - 1)
	except:
		break

vis = [False] * len(graph)

def dfs(u):
	vis[u] = True
	for v in graph[u]:
		if not vis[v]:
			dfs(v)

res = 0
for i in range(len(graph)):
	if not vis[i]:
		dfs(i)
		res += 1

print(res - 1)
