from sys import stdin
def read_fasta(file = stdin):
	res = {}
	key = ''
	while True:
		try:
			s = file.readline().strip()
		except:
			break

		if not s:
			break
		
		if s[0] == '>':
			key = s[1:]
			res[key] = ''
		else:
			res[key] += s
	return res

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

def translate(s, x = 0):
	res = ''
	for i in range(x, len(s), 3):
		if (i + 3) > len(s):
			break
		if m[s[i: i + 3]] == 'Stop':
			yield res
			res = ''
		else:
			res += m[s[i: i + 3]]

def transcript(s):
	return s.replace('T', 'U')
