from queue import Queue
from sys import setrecursionlimit
setrecursionlimit(int(1e7))
memo = {}

q = Queue()
q.put(('0123456789', 0))
memo['0123456789'] = 0
while not q.empty():
	x, d = q.get()
	memo[x] = d

	for i in range(10):
		for j in range(i + 1, 10):
			t = x[:i] + x[i: j + 1][::-1] + x[j + 1:]
			if t not in memo:
				memo[t] = int(1e9)
				q.put((t, d + 1))

for i in range(5):
	if i:
		input()
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))

	l = [0] * 10
	for i in range(10):
		l[a[i] - 1] = i
	
	# print(a, b, ''.join(str(l[i - 1]) for i in b))
	print(memo[''.join(str(l[i - 1]) for i in b)], end = ' ')
