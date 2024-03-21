from utils import read_fasta
from functools import cache

l = list(read_fasta().values())

s = ''
res = ''
for i in range(len(l[0])):
	s += l[0][i]
	while not all(s in i for i in l):
		s = s[1:]
	if len(s) > len(res):
		res = s
print(res)
