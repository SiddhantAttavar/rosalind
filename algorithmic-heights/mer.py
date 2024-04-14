n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

res = []
i = 0
j = 0
while i < len(a) or j < len(b):
	if j == len(b) or (i < len(a) and a[i] <= b[j]):
		res.append(a[i])
		i += 1
	else:
		res.append(b[j])
		j += 1
print(*res)
