n = int(input())
a = [input() for _ in range(n)]
l = []
while True:
	try:
		l.append(float(input()))
	except:
		break


m = {
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

res = 0
p = ''
for s in a:
	v = [0]
	x = 0
	for c in s:
		x += m[c]
		v.append(x)

	x = 0
	for c in s[::-1]:
		x += m[c]
		v.append(x)
	v.pop()

	d = {}
	for i in v:
		for j in l:
			y = round(i - j, 5)
			d[y] = d.get(y, 0) + 1
	
	k = max(d.values())
	if k >= res:
		res = k
		p = s

print(res)
print(p)
