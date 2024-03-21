from utils import read_fasta, translate, transcript

s = list(read_fasta().values())
x = s[0]
for i in s[1:]:
	x = x.replace(i, '')
x = transcript(x)

print(*translate(x, 0))
