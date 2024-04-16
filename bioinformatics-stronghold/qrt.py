a = input().split()
l = []
while True:
	try:
		l.append(input())
	except:
		break

res = set()
for s in l:
	x = []
	y = []
	for i in range(len(s)):
		if s[i] == '1':
			x.append(a[i])
		elif s[i] == '0':
			y.append(a[i])
	
	if min(len(x), len(y)) < 2:
		continue

	x.sort()
	y.sort()
	for i in range(len(x)):
		for j in range(i + 1, len(x)):
			for p in range(len(y)):
				for q in range(p + 1, len(y)):
					c = ((x[i], x[j]), (y[p], y[q]))
					if c[0] > c[1]:
						c = (c[1], c[0])
					res.add(c)

for (x, y), (a, b) in res:
	print('{' + str(x) + ', ' + str(y) + '} {' + str(a) + ', ' + str(b) + '}')
