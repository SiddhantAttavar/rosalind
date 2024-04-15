s = input()

a = {'A': [], 'C': [], 'T': [], 'G': [], '$': []}
for i in range(len(s)):
	a[s[i]].append(i)

res = 1
for c, l in a.items():
	x = 1
	while len(l) > 0 and max(l) < len(s):
		for i in l:
			if s[i] != s[l[0]]:
				break
		else:
			x += 1
			for i in range(len(l)):
				l[i] += 1
			continue
		break
	res *= x

print(res)
