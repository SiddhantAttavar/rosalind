from math import log10

n = int(input())
x = 0
res = []
k = 1
y = pow(0.5, 2 * n)
for i in range(2*n, 0, -1):
	x += k * y
	res.append(round(log10(x), 3))
	k = (k * i) // (2 * n - i + 1)
print(*res[::-1])
