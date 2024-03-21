from itertools import permutations

n = int(input())
l = list(permutations(range(1, n + 1)))
print(len(l))
print(*[' '.join(map(str, i)) for i in l], sep = '\n')
