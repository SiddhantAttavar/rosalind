k, n = map(int, input().split())
for _ in range(k):
	a = list(map(int, input().split()))
	d = {}
	for i in range(n):
		if -a[i] in d:
			print(*d[-a[i]], i + 1)
			break
		for j in range(i):
			d[a[j] + a[i]] = (j + 1, i + 1)
	else:
		print(-1)
