from queue import Queue
from sys import setrecursionlimit
setrecursionlimit(int(1e7))
memo = {}

q = Queue()
q.put(('0123456789', 0))
memo['0123456789'] = 0, -1, -1
while not q.empty():
	x, d = q.get()

	for i in range(10):
		for j in range(i + 1, 10):
			t = x[:i] + x[i: j + 1][::-1] + x[j + 1:]
			if t not in memo:
				memo[t] = d + 1, i, j
				q.put((t, d + 1))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

l = [0] * 10
for i in range(10):
	l[a[i] - 1] = i

# print(a, b, ''.join(str(l[i - 1]) for i in b))
s = ''.join(str(l[i - 1]) for i in b)
res = []
while memo[s][1] != -1:
	res.append((memo[s][1], memo[s][2]))
	s = s[:memo[s][1]] + s[memo[s][1]: memo[s][2] + 1][::-1] + s[memo[s][2] + 1:]

print(len(res))
res.reverse()
for i in res:
	print(i[0] + 1, i[1] + 1)
