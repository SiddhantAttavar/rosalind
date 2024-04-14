from heapq import _heapify_max
input()
a = list(map(int, input().split()))
_heapify_max(a)
print(*a)
