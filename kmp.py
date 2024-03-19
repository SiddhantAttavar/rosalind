from utils import read_fasta
s = list(read_fasta().values())[0]
p = [0] * len(s)
p[0] = 0
x = 0

for i in range(1, len(s)):
	while x and s[x] != s[i]:
		x = p[x - 1]

	if s[x] == s[i]:
		x += 1
		p[i] = x

print(*p)
