from utils import read_fasta

m = {
	'UUU': 'F',
	'CUU': 'L',
	'AUU': 'I',
	'GUU': 'V',
	'UUC': 'F',
	'CUC': 'L',
	'AUC': 'I',
	'GUC': 'V',
	'UUA': 'L',
	'CUA': 'L',
	'AUA': 'I',
	'GUA': 'V',
	'UUG': 'L',
	'CUG': 'L',
	'AUG': 'M',
	'GUG': 'V',
	'UCU': 'S',
	'CCU': 'P',
	'ACU': 'T',
	'GCU': 'A',
	'UCC': 'S',
	'CCC': 'P',
	'ACC': 'T',
	'GCC': 'A',
	'UCA': 'S',
	'CCA': 'P',
	'ACA': 'T',
	'GCA': 'A',
	'UCG': 'S',
	'CCG': 'P',
	'ACG': 'T',
	'GCG': 'A',
	'UAU': 'Y',
	'CAU': 'H',
	'AAU': 'N',
	'GAU': 'D',
	'UAC': 'Y',
	'CAC': 'H',
	'AAC': 'N',
	'GAC': 'D',
	'UAA': 'Stop',
	'CAA': 'Q',
	'AAA': 'K',
	'GAA': 'E',
	'UAG': 'Stop',
	'CAG': 'Q',
	'AAG': 'K',
	'GAG': 'E',
	'UGU': 'C',
	'CGU': 'R',
	'AGU': 'S',
	'GGU': 'G',
	'UGC': 'C',
	'CGC': 'R',
	'AGC': 'S',
	'GGC': 'G',
	'UGA': 'Stop',
	'CGA': 'R',
	'AGA': 'R',
	'GGA': 'G',
	'UGG': 'W',
	'CGG': 'R',
	'AGG': 'R',
	'GGG': 'G' 
}

def translate(s, x):
	res = ''
	for i in range(x, len(s), 3):
		if (i + 3) > len(s):
			break
		if m[s[i: i + 3]] == 'Stop':
			yield res
			res = ''
		else:
			res += m[s[i: i + 3]]

def revc(s):
	d = {
		'A': 'T',
		'T': 'A',
		'C': 'G',
		'G': 'C',
	}
	res = ''
	for c in s:
		res += d[c]
	return res[::-1]

s = list(read_fasta().values())[0]
t = revc(s)
s = s.replace('T', 'U')
t = t.replace('T', 'U')

l = []
for i in range(3):
	l += list(translate(s, i)) + list(translate(t, i))
res = set()
for s in l:
	for j in range(len(s) - 1, -1, -1):
		if s[j] == 'M':
			res.add(s[j:])
print(*res, sep = '\n')
