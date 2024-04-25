from collections import Counter
l = list(map(int, input().split()))

x = max(l)
res = []
d = Counter(l)

while d:
	y = max(d)

	b = Counter(abs(y - i) for i in res)

	if any(b[i] > d[i] for i in b):
		y = x - y
		b = Counter(abs(y - i) for i in res)
	
	res.append(y)
	d -= b

print(*sorted(res))
