l = list(map(int, input().split()))

res = []
for i in range(len(l)):
	for j in range(i + 1, len(l)):
		res.append(l[j] - l[i])
res.sort()

ans = []
with open('in.txt') as f:
	ans = sorted(map(int, f.read().split()))

if len(res) == len(ans):
	for i in range(len(res)):
		if res[i] != ans[i]:
			print(i)
else:
	print(len(res), len(ans))

