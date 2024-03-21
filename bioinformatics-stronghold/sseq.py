from utils import read_fasta

s, t = read_fasta().values()

j = 0
res = []
for i in range(len(s)):
	if s[i] == t[j]:
		j += 1
		res.append(i + 1)
		if j == len(t):
			break
print(*res)
