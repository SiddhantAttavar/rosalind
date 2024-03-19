a, b, c = map(int, input().split())
print(1 - (c * (c - 1) + b * c + b * (b - 1) / 4) / ((a + b + c) * (a + b + c - 1)))

