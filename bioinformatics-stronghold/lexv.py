s = input().split()
n = int(input())

l = [[] for _ in range(n)]
l[0] = [[i] for i in range(len(s))]
for i in range(1, n):
	for j in l[i - 1]:
		for k in range(len(s)):
			l[i].append(j + [k])

res = []
for i in l:
	res += i
res.sort()

for i in res:
	t = ''
	for j in i:
		t += s[j]
	print(t)
