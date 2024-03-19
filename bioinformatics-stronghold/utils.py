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
