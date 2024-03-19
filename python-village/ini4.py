pref_odd_sum = lambda x: ((x + 1) // 2) ** 2
a , b = map(int, input().split())
print(pref_odd_sum(b) - pref_odd_sum(a - 1))
