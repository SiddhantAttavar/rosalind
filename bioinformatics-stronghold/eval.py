n = int(input())
s = input()
x = s.count('G') + s.count('C')

for i in map(float, input().split()):
	print(pow(i / 2, x) * pow((1 - i) / 2, len(s) - x) * (n - len(s) - 1), end = ' ')
