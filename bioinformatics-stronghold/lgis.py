def bisect(a, i, comp):
	l, r = 0, len(a) - 1
	res = len(a)
	while l <= r:
		m = (l + r) // 2
		if comp(i, a[m]):
			res = m
			r = m - 1
		else:
			l = m + 1
	return res

# from bisect import bisect

n = int(input())
l = list(map(int, input().split()))

def lis(v, comp):
	l = [i - 1 for i in v]
	a = []
	p = [-1] * len(l)
	m = -1
	for i in l:
		j = bisect(a, i, comp)
		if j == len(a):
			a.append(i)
			m = i
		else:
			a[j] = i
		if j:
			p[i] = a[j - 1]
	
	res = [m]
	while len(res) < len(a):
		res.append(p[res[-1]])
	
	return [i + 1 for i in res[::-1]]

print(*lis(l, lambda x, y: x < y))
print(*lis(l, lambda x, y: x > y))
