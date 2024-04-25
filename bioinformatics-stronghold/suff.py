s = input()
s += '$'

res = []
def solve(l):
	if len(l) == 0:
		return

	t = ''
	while max(l) < len(s):
		for i in l:
			if s[i] != s[l[0]]:
				break
		else:
			t += s[l[0]]
			for i in range(len(l)):
				l[i] += 1
			continue
		break

	res.append(t)

	a = {'A': [], 'C': [], 'T': [], 'G': [], '$': []}
	for i in l:
		if i < len(s):
			a[s[i]].append(i)

	for i in a.values():
		solve(i)


l = list(range(len(s)))
a = {'A': [], 'C': [], 'T': [], 'G': [], '$': []}
for i in l:
	a[s[i]].append(i)

for i in a.values():
	solve(i)
print(*sorted(res), sep = '\n')
