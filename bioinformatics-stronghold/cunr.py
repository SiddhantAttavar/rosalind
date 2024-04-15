res = 1
for i in range(3, 2 * int(input()) - 4, 2):
	res = (res * i) % 1_000_000
print(res)
