d = {
	'A': 71.03711,
	'C': 103.00919,
	'D': 115.02694,
	'E': 129.04259,
	'F': 147.06841,
	'G': 57.02146,
	'H': 137.05891,
	'I': 113.08406,
	'K': 128.09496,
	'L': 113.08406,
	'M': 131.04049,
	'N': 114.04293,
	'P': 97.05276,
	'Q': 128.05858,
	'R': 156.10111,
	'S': 87.03203,
	'T': 101.04768,
	'V': 99.06841,
	'W': 186.07931,
	'Y': 163.06333 ,
}

x = float(input())
l = []
while True:
	try:
		l.append(float(input()))
	except:
		break
l.sort()

j = l[0]
res = ''

v = [0] * len(l)
v[0] = 1
v[-1] = -1

for i in range(1, len(l)):
	if v[i] == -1:
		continue

	y = l[i] - j
	m = 1e9
	u = ''
	for k, z in d.items():
		if abs(y - z) < m:
			m = abs(y - z)
			u = k
	
	if m < 1e-5 or v[i] == 1:
		res += u
		j = l[i]
		if i < len(l) // 2:
			v[-i - 1] = -1
	else:
		v[-i - 1] = 1

print(res)
