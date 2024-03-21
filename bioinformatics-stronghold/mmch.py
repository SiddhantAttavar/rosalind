from utils import read_fasta
from math import factorial

s = list(read_fasta().values())[0]
a = s.count('A')
u = s.count('U')
c = s.count('C')
g = s.count('G')

comb = lambda n, r: factorial(n) // factorial(n - r)
print(comb(max(a, u), min(a, u)) * comb(max(c, g), min(c, g)))
