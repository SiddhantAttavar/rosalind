from math import log10
def calc_prob(s, x):
	y = s.count('G') + s.count('C')
	return y * log10(x / 2) + (len(s) - y) * log10((1 - x) / 2)

s = input()
a = list(map(float, input().split()))
print(*[calc_prob(s, i) for i in a])
