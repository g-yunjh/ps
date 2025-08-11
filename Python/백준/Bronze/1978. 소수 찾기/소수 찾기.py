n = int(input())
t = list(map(int, input().split()))

for i in t:
    if i == 1:
        n = n-1
        continue
    else:
        for _ in range(2,i):
            if i%_ == 0:
                n -= 1
                break

print(n)