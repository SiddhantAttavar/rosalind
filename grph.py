from collections import defaultdict
v = []
pref = defaultdict(lambda: [])
suff = defaultdict(lambda: [])
while True:
	try:
		s = input()
		if not s or s[0] != '>':
			break
		v.append(s[1:])
		x = input()
		pref[x[:3]].append(len(v) - 1)
		suff[x[len(x) - 3:]].append(len(v) - 1)
	except:
		break
for s in pref:
	for i in pref[s]:
		for j in suff[s]:
			if i != j:
				print(v[j], v[i])
