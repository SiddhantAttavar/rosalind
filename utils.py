def read_fasta():
	res = {}
	key = ''
	while True:
		try:
			s = input()
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
