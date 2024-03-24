from utils import read_fasta, revc
from collections import defaultdict

l = list(read_fasta().values())
m = defaultdict(lambda: 0)
for i in l:
	m[i] += 1
	m[revc(i)] += 1

v = {i for i in m if m[i] > 1}

for i in l:
	if m[i] > 1:
		continue
	for j in v:
		flag = False
		for k in range(len(i)):
			if i[k] != j[k]:
				if flag:
					break
				flag = True
		else:
			print(f'{i}->{j}')
			break
