t = int(input())
for i in range(t):
	n, m = map(int, input().split())
	cnt = 1
	for i in range(n):
		cnt *= m - i
		cnt /= i + 1
	print(int(cnt))