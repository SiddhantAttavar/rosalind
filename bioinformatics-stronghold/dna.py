s = input()
d = 'ACGT'
m = {i: 0 for i in d}
for c in s:
	m[c] += 1
print(*[m[i] for i in d])
