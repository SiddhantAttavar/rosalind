k = input().split()
l = []
while True:
	try:
		l.append(input())
	except:
		break
l = [list(map(int, i)) for i in l]

a = set(range(len(l)))
b = set(range(len(l[0])))
s = [sum(i) for i in l]

while a:
	u, x = 0, 0
	for i in a:
		if s[i] == 2:
			u = i
			x = 1
		elif s[i] == len(b) - 2:
			u = i
			x = 0
	
	p, q = [i for i in b if l[u][i] == x]
	k[p] = f'({k[p]},{k[q]})'
	b.remove(q)

	v = []
	for i in a:
		s[i] -= l[i][q]
		if s[i] == 1 or s[i] == len(b) - 1:
			v.append(i)
	for i in v:
		a.remove(i)

print(f'({",".join(k[i] for i in b)});')
