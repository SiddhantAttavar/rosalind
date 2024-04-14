import numpy as np
import networkx as nx

def reverse_symbol(a):
    return (a == 0).astype(int)
        
v = []
while True:
	try:
		v.append(input())
	except:
		break
table = v
mat = np.array([list(i.rstrip()) for i in table], dtype=int)
n = len(table)

G = nx.Graph()
for i in range(n-1):
    for j in range(1, n):
        a = mat[i] + mat[j]
        b = mat[i] + reverse_symbol(mat[j])
        if 0 in a and 2 in a and 0 in b and 2 in b:
            G.add_edge(i, j)

table.pop(nx.center(G)[0])           
print(*table, sep = '\n')
