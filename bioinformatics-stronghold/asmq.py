l = []
while True:
	try:
		l.append(len(input()))
	except:
		break

l.sort(reverse = True)
s = sum(l)

i = -1
x = 0
while 2 * x < s:
	i += 1
	x += l[i]

j = -1
y = 0
while 4 * y < 3 * s:
	j += 1
	y += l[j]

print(l[i], l[j])
