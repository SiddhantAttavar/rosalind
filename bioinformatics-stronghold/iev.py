p = [1, 1, 1, 3 / 4, 1 / 2, 0]
l = list(map(int, input().split()))
print(2 * sum([p[i] * l[i] for i in range(6)]))
