from utils import read_fasta
from math import factorial

s = list(read_fasta().values())[0]
a = s.count('A')
u = s.count('U')
c = s.count('C')
g = s.count('G')
if a == u and c == g:
	print(factorial(a) * factorial(c))
else:
	print(0)
