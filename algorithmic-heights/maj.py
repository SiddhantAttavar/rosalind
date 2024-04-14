k, n = map(int, input().split())
for _ in range(k):
	a = list(map(int, input().split()))
	d = {}
	for i in a:
		d[i] = d.get(i, 0) + 1
	k, x = max(d.items(), key = lambda y: y[1])
	if 2 * x > n:
		print(k, end = ' ')
	else:
		print(-1, end = ' ')
