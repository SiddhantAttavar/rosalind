a = input().split()
l = []

while True:
	try:
		l.append(input())
	except:
		break

x = 1
while x < len(a):
	x *= 2

tree = [[] for _ in range(2 * x)]
for i in range(x - 1):
	tree[i] = [2 * i, 2 * i + 1]

names = [[] for i in range(2 * x)]

def construct_tree(names, j):
	res = []

	if j == len(l[0]):


	a = []
	b = []

for j in range(len(l[0])):
	y = 1
	for i in l:
		y *= 2
		if i[j] == '1':
			y += 1
	names[y].append(a[j])

def write_newick(u):
	if len(names[u]) == 1:
		return names[u][0]
	
	if len(names[u]) == 2:
		return f'({names[u][0]},{names[u][1]})'
	
	return f'({write_newick(2 * u)},{write_newick(2 * u + 1)})'

print(f'{write_newick(1)};')
