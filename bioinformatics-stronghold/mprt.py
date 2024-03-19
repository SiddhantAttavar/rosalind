from requests import get

def get_motif_locs(s, t):
	res = []
	for i in range(len(s)):
		j = i
		k = 0
		while k < len(t) and j < len(s):
			if s[j] == t[k]:
				j += 1
				k += 1
				continue

			if t[k] == '[':
				k += 1
				flag = False
				while t[k] != ']':
					if s[j] == t[k]:
						flag = True
					k += 1

				if not flag:
					break

				j += 1
				k += 1
				continue

			if t[k] == '{':
				k += 1
				while t[k] != '}':
					if s[j] == t[k]:
						break
					k += 1
				else:
					j += 1
					k += 1
					continue
				break

			break
		else:
			if k == len(t):
				res.append(i + 1)
	return res


l = {}
while True:
	try:
		s = input()
		f = get(f'https://rest.uniprot.org/uniprotkb/{s.split("_")[0]}.fasta').text.split('\n')
		l[s] = ''.join(f[1:])
	except:
		break

for k, v in l.items():
	# print(k)
	# print(v)
	res = get_motif_locs(v, 'N{P}[ST]{P}')
	if res:
		print(k)
		print(*res)
