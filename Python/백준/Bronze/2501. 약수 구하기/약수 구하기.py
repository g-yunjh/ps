n, k = map(int, input().split())
p = []

for i in range(1, n+1):
    if n % i == 0:
        p.append(i)

if len(p) >= k:
    print(p[k-1])
else:
    print(0)