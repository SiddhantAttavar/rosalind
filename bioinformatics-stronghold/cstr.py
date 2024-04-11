l = []
while True:
	try:
		l.append(input())
	except:
		break

for j in range(len(l[0])):
	res = ''
	for i in range(len(l)):
		if l[i][j] == l[0][j]:
			res += '1'
		else:
			res += '0'
	
	x = res.count('1')
	if 1 < x and x < len(l) - 1:
		print(res)

