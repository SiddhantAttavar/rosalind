from utils import read_fasta
x = ''
m = 0
for k, v in read_fasta().items():
	c = (v.count('G') + v.count('C')) / len(v)
	if c > m:
		m = c
		x = k
print(x)
print(m * 100)
