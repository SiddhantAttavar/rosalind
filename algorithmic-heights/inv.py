class SegTree:
	def __init__(self, n):
		self.a = [0] * (4 * n)
	
	def update(self, c, l, r, i):
		if i < l or r < i:
			return

		if l == r:
			self.a[c] += 1
			return

		m = (l + r) // 2
		self.update(2 * c + 1, l, m, i)
		self.update(2 * c + 2, m + 1, r, i)
		self.a[c] = self.a[2 * c + 1] + self.a[2 * c + 2]
	
	def query(self, c, l, r, s, e):
		if e < l or r < s:
			return 0
		
		if s <= l and r <= e:
			return self.a[c]

		m = (l + r) // 2
		return (
			self.query(2 * c + 1, l, m, s, e) +
			self.query(2 * c + 2, m + 1, r, s, e)
		)

n = int(input())
a = list(map(int, input().split()))

res = 0
s = SegTree(int(2e5) + 1)
for i in a:
	res += s.query(0, 0, int(2e5), i + int(1e5) + 1, int(2e5))
	s.update(0, 0, int(2e5), i + int(1e5))
print(res)
