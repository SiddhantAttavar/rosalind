for _ in range(int(input())):
	# input()
	n, m = map(int, input().split())
	e = []
	for _ in range(m):
		u, v, w = map(int, input().split())
		e.append((u - 1, v - 1, w))

	d = [int(1e9)] * n
	d[0] = 0
	for i in range(n - 1):
		for u, v, w in e:
			if d[v] > d[u] + w:
				d[v] = d[u] + w

	for u, v, w in e:
		if d[v] > d[u] + w:
			print(1, end = ' ')
			break
	else:
		print(-1, end = ' ')