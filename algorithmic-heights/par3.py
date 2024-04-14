n = int(input())
a = list(map(int, input().split()))
x = []
y = []
z = []
for i in a:
	if i < a[0]:
		x.append(i)
	elif i == a[0]:
		y.append(i)
	else:
		z.append(i)
print(*(x + y + z))
