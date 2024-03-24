from utils import read_fasta

a, b = read_fasta().values()
x = y = 0
m = {
	'A': 'G',
	'T': 'C',
	'C': 'T',
	'G': 'A',
}
for i in range(len(a)):
	if a[i] == b[i]:
		continue
	if m[a[i]] == b[i]:
		x += 1
	else:
		y += 1
print(x / y)
