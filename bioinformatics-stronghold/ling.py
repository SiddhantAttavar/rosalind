s = input()
s += '$'

class Node:
	def __init__(self, sub="", children=None):
		self.sub = sub
		self.ch = children or []

class SuffixTree:
	def __init__(self, str):
		self.nodes = [Node()]
		for i in range(len(str)):
			self.addSuffix(str[i:])

	def addSuffix(self, suf):
		n = 0
		i = 0
		while i < len(suf):
			b = suf[i]
			x2 = 0
			while True:
				children = self.nodes[n].ch
				if x2 == len(children):
					# no matching child, remainder of suf becomes new node
					n2 = len(self.nodes)
					self.nodes.append(Node(suf[i:], []))
					self.nodes[n].ch.append(n2)
					return
				n2 = children[x2]
				if self.nodes[n2].sub[0] == b:
					break
				x2 = x2 + 1

			# find prefix of remaining suffix in common with child
			sub2 = self.nodes[n2].sub
			j = 0
			while j < len(sub2):
				if suf[i + j] != sub2[j]:
					# split n2
					n3 = n2
					# new node for the part in common
					n2 = len(self.nodes)
					self.nodes.append(Node(sub2[:j], [n3]))
					self.nodes[n3].sub = sub2[j:] # old node loses the part in common
					self.nodes[n].ch[x2] = n2
					break # continue down the tree
				j = j + 1
			i = i + j   # advance past part in common
			n = n2	  # continue down the tree

	def get_distinct(self):
		if len(self.nodes) == 0:
			return 0

		def f(n):
			children = self.nodes[n].ch
			if len(children) == 0:
				return len(self.nodes[n].sub) - 1
			res = len(self.nodes[n].sub)
			for c in children:
				res += f(c)
			return res

		return f(0)

t = SuffixTree(s)
x = 1
y = 0
n = len(s) - 1
for k in range(1, n + 1):
	if x <= n:
		x *= 4
	y += min(x, n - k + 1)
print(t.get_distinct() / y)
