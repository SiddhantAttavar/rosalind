n = int(input())
a = set(map(int, input()[1:-1].split(', ')))
b = set(map(int, input()[1:-1].split(', ')))

print(a.union(b))
print(a.intersection(b))
print(a - b)
print(b - a)
print(set(range(1, n + 1)) - a)
print(set(range(1, n + 1)) - b)
