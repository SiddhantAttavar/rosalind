v = []
while True:
	try:
		v.append(input())
	except:
		break
l = [int(i, 2) for i in v]

u = -1
for i in range(len(l)):
	for j in range(len(l)):
		if j == i:
			continue
		for k in range(j):
			if k != i and l[j] & l[k] and l[j] & l[k] != min(l[j], l[k]):
				break
		else:
			continue
		break
	else:
		u = i
		break

print(*[v[i] for i in range(len(v)) if i != u], sep = '\n')
