l = input().split()
n = int(input())

res = ['']
for i in range(n):
	n_res = []
	for j in res:
		for k in l:
			n_res.append(j + k)
	res = n_res
print(*res, sep = '\n')
