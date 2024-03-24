from utils import read_fasta

l = list(read_fasta().values())
res = [[0] * len(l) for _ in range(len(l))]
for i in range(len(l)):
	for j in range(len(l)):
		for k in range(len(l[i])):
			res[i][j] += l[i][k] != l[j][k]
		res[i][j] /= len(l[i])

for i in res:
	print(*i)
