from utils import read_fasta

l = list(read_fasta().values())

while len(l) > 1:

	m = (-1, -1)
	x = 0
	for i in range(len(l)):
		for j in range(len(l)):
			if i == j:
				continue

			for k in range(min(len(l[i]), len(l[j])), x, -1):
				if l[i][:k] == l[j][len(l[j]) - k:]:
					m = (i, j)
					x = k
					break

	s = l[m[1]] + l[m[0]][x:]
	if m[0] < m[1]:
		m = (m[1], m[0])
	
	l.pop(m[0])
	l.pop(m[1])
	l.append(s)

print(l[0])
