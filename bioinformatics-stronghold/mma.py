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

rm = {}
for k, v in m.items():
	if v not in rm:
		rm[v] = 1
	else:
		rm[v] += 1

x = 1
mod = 1_000_000
for c in input():
	x = (x * rm[c]) % mod
print((x * rm['Stop']) % mod)
