from utils import read_fasta
l = list(read_fasta().values())
m = {c: [0] * len(l[0]) for c in 'ATCG'}
for s in l:
	for i in range(len(s)):
		m[s[i]][i] += 1

res = ''
for i in range(len(s)):
	c = 'A'
	for j in 'TCG':
		if m[j][i] > m[c][i]:
			c = j
	res += c
print(res)
for c in 'ACGT':
	print(f'{c}: {" ".join(map(str, m[c]))}')
