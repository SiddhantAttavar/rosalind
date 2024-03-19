from collections import defaultdict
from utils import read_fasta
v = []

l = list(read_fasta().items())

pref = defaultdict(lambda: [])
suff = defaultdict(lambda: [])

for i in range(len(l)):
	pref[l[i][1][:3]].append(i)
	suff[l[i][1][len(l[i][1]) - 3:]].append(i)
	
for s in pref:
	for i in pref[s]:
		for j in suff[s]:
			if i != j:
				print(l[j][0], l[i][0])
