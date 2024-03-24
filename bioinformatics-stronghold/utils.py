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

def _parse_newick_util(s, i, names, trees):
	weight = ''
	while s[i].isdigit():
		weight += s[i]
		i += 1
	if s[i] != ':':
		weight = '1'
	else:
		i += 1
	weight = int(weight[::-1])
	
	name = ''
	while s[i] not in '(),':
		name += s[i]
		i += 1

	j = len(trees)
	names.append(name[::-1])
	trees.append([])
	
	if s[i] != ')':
		return i, j, weight

	while s[i] in ',)':
		i, v, w = _parse_newick_util(s, i + 1, names, trees)
		trees[j].append((v, w))
	i += 1

	return i, j, weight
	
def parse_newick(s):
	names = []
	trees = []

	s = s[::-1]
	i = s[0] == ';'
	while i < len(s):
		i, _, _ = _parse_newick_util(s, i + (s[i] in ',;'), names, trees)

	new_trees = [[] for _ in range(len(trees))]
	for u in range(len(trees)):
		for v, w in trees[u]:
			new_trees[u].append((v, w))
			new_trees[v].append((u, w))

	return names, new_trees

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
