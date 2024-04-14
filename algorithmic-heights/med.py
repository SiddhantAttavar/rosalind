n = int(input())
a = list(map(int, input().split()))
k = int(input())

def solve(a, k):
	if k == 1:
		return a[0]

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
	
	if k <= len(x):
		return solve(x, k)
	if k <= len(x) + len(y):
		return a[0]
	return solve(z, k - len(x) - len(y))

print(solve(a, k))
