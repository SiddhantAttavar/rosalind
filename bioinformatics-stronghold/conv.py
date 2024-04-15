a = list(map(float, input().split()))
b = list(map(float, input().split()))
d = {}
for i in a:
	for j in b:
		x = round(i - j, 5)
		d[x] = d.get(x, 0) + 1
k, v = max(d.items(), key = lambda x: x[1])
print(v)
print(abs(k))
