n = int(input())
m = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for x in b:
	l = 0
	r = n - 1
	res = -1
	while l <= r:
		m = (l + r) // 2
		if a[m] == x:
			res = m + 1
			break
		elif a[m] < x:
			l = m + 1
		else:
			r = m - 1
	print(res, end = ' ')
