from decimal import Decimal
t = input().split()
n, x = int(t[0]), float(t[1])
s = input()

p = 1;
for c in s:
	if c in 'GC':
		p *= x / 2
	else:
		p *= (1 - x) / 2
print(1 - (1 - p) ** n)
