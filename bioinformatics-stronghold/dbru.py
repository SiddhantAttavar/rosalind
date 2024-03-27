from utils import revc

graph = set()
while True:
	try:
		s = input()
		graph.add((s[:-1], s[1:]))
		s = revc(s)
		graph.add((s[:-1], s[1:]))
	except:
		break

for i, j in graph:
	print(f'({i}, {j})')
