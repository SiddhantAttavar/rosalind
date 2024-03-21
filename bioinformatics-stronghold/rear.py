for i in range(5):
	if i:
		input()
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))

	res = 0
	for i in range(len(b)):
		if a[i] == b[i]:
			continue

		res += 1
		j = -1
		for k in range(i + 1, len(b)):
			if b[k] == a[i]:
				j = k
				break

		for k in range(i, (i + j + 1) // 2):
			b[k], b[i + j - k] = b[i + j - k], b[k]
	print(res, end = ' ')
