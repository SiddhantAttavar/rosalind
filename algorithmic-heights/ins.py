n = int(input())
a = list(map(int, input().split()))

res = 0
for i in range(n):
	for j in range(i, 0, -1):
		if a[j] >= a[j - 1]:
			break
		res += 1
		a[j], a[j - 1] = a[j - 1], a[j]
print(res)
