from sys import setrecursionlimit
setrecursionlimit(int(1e6))
l = input().split()

def solve(x):
	if len(x) == 1:
		return [l[x[0]]]

	res = []
	for i in range(1 << (len(x) - 1)):
		a = [x[-1]]
		b = []

		for j in range(len(x) - 1):
			if i & (1 << j):
				b.append(x[j])
			else:
				a.append(x[j])

		if min(len(a), len(b)) == 0:
			continue
		
		for s in solve(a):
			for t in solve(b):
				res.append(f'({s},{t})')

	return res

for s in solve(range(1, len(l))):
	print(f'({s}){l[0]};')
