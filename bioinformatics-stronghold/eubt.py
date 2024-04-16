from sys import setrecursionlimit
setrecursionlimit(int(1e6))
l = input().split()

def solve(x):
	if len(x) == 1:
		return [l[x[0]]]

	res = []
	flag = x[0] == 1
	for i in range(1 << (len(x) - flag)):
		a = [1] if flag else []
		b = []

		for j in range(len(x) - flag):
			if i & (1 << j):
				b.append(x[j + flag])
			else:
				a.append(x[j + flag])

		if min(len(a), len(b)) == 0:
			continue
		
		for s in solve(a):
			for t in solve(b):
				res.append(f'({s},{t})')

	return res

for s in solve(range(1, len(l))):
	print(f'{s}{l[0]};')
