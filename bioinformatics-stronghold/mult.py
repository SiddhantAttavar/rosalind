from functools import cache
from utils import read_fasta

l = list(read_fasta().values())

@cache
def solve(x):
	if x == (0,) * len(l):
		return 0, [''] * len(l)

	res = -int(1e9)
	m = [''] * len(l)
	for i in range(1, 1 << len(l)):
		y = []
		s = []
		for j in range(len(l)):
			if i & (1 << j):
				if x[j] == 0:
					break
				y.append(x[j] - 1)
				s.append(l[j][x[j] - 1])
			else:
				y.append(x[j])
				s.append('-')
		else:
			k = 0
			for a in range(len(l)):
				for b in range(a):
					k -= s[a] != s[b]
			t, c = solve(tuple(y))
			if t + k > res:
				res = t + k
				m = [c[i] + s[i] for i in range(len(l))]
	
	return res, m

x, res = solve(tuple(len(i) for i in l))
print(x)
print(*res, sep = '\n')
