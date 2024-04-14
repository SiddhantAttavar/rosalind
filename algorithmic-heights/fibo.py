a = [1, 1, 1, 0]

def matmul(a, b):
	return [
		a[0] * b[0] + a[1] * b[2],
		a[0] * b[1] + a[1] * b[3],
		a[2] * b[0] + a[3] * b[2],
		a[2] * b[1] + a[3] * b[3]
	]

def matpow(a, x):
	res = [1, 0, 0, 1]
	while x:
		if x & 1:
			res = matmul(res, a)

		a = matmul(a, a)
		x >>= 1
	return res

n = int(input())
print(matpow(a, n - 1)[0])
