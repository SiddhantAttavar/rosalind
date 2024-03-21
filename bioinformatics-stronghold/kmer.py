from utils import read_fasta

s = list(read_fasta().values())[0]
a = ['ACGT'.index(c) for c in s]

res = [0] * (4 ** 4)
for i in range(len(a) - 3):
	x = 0
	for j in range(i, i + 4):
		x = 4 * x + a[j]
	res[x] += 1

print(*res)
