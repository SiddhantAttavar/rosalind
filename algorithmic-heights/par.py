n = int(input())
a = list(map(int, input().split()))
x = []
y = []
for i in a[1:]:
	if i <= a[0]:
		x.append(i)
	else:
		y.append(i)
x.append(a[0])
print(*(x + y))
