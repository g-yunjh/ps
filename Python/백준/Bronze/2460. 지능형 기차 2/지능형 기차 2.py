count = 0
max = 0

for i in range(10):
    n, m = map(int, input().split())
    count = count - n + m
    if count > max:
        max = count
    else:
        continue

print(max)