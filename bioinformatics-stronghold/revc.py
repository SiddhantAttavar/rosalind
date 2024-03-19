s = input()
m = {
	'A': 'T',
	'T': 'A',
	'C': 'G',
	'G': 'C',
}
res = ''
for c in s:
	res += m[c]
print(res[::-1])
