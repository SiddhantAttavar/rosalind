s = input()
t = input()
x = 0
for i in range(len(s)):
	x += s[i] == t[i]
print(len(s) - x)
